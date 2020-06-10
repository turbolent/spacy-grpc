import logging
from concurrent import futures
from typing import Optional

import click as click
import grpc
import spacy
from spacy.language import Language
from spacy.tokens import Doc, Token

from spacy_grpc import spacy_pb2, spacy_pb2_grpc


class SpaCy(spacy_pb2_grpc.SpaCyServicer):

    def __init__(self, tagging_nlp: Language, ner_nlp: Language) -> None:
        self.tagging_nlp = tagging_nlp
        self.ner_nlp = ner_nlp

    @classmethod
    def _lemma(cls, token: Token) -> str:
        if token.lemma_ != "-PRON-":
            return token.lemma_.lower().strip()
        else:
            return token.lower_

    def Tag(self, request: spacy_pb2.Request, context: grpc.ServicerContext) -> spacy_pb2.Reply:
        document: Doc = self.tagging_nlp(request.sentence)
        element: Token
        return spacy_pb2.Reply(
            tokens=[
                spacy_pb2.Token(
                    text=element.orth_,
                    tag=element.tag_,
                    lemma=self._lemma(element)
                )
                for element in document
            ]
        )

    @classmethod
    def _entity(cls, token: Token) -> Optional[str]:
        if not token.ent_type_:
            return None
        else:
            return '-'.join([token.ent_iob_, token.ent_type_])

    def NER(self, request: spacy_pb2.Request, context: grpc.ServicerContext) -> spacy_pb2.Reply:
        document: Doc = self.ner_nlp(request.sentence)
        element: Token
        return spacy_pb2.Reply(
            tokens=[
                spacy_pb2.Token(
                    text=token.orth_,
                    tag=token.tag_,
                    lemma=self._lemma(token),
                    entity=self._entity(token)
                )
                for token in document
            ]
        )


@click.command()
@click.option(
    '--port',
    type=int,
    default=9090,
    show_default=True
)
@click.option(
    '--language',
    type=str,
    default='en_core_web_sm',
    show_default=True
)
def serve(port: int, language: str) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info("Loading ...")

    tagging_nlp: Language = spacy.load(language, disable=['ner'])
    tagging_nlp.remove_pipe('parser')
    logging.info("Tagging pipeline: %s", ', '.join(tagging_nlp.pipe_names))

    ner_nlp: Language = spacy.load(language)
    logging.info("NER pipeline: %s", ', '.join(ner_nlp.pipe_names))

    server = grpc.server(futures.ThreadPoolExecutor())
    spacy_pb2_grpc.add_SpaCyServicer_to_server(SpaCy(tagging_nlp, ner_nlp), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info("Serving on port %d ...", port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve(auto_envvar_prefix='SPACY')