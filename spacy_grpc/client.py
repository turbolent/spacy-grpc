from typing import Callable

import click
import grpc
from tabulate import tabulate

import spacy_pb2
import spacy_pb2_grpc

DEFAULT_PORT = 9090

Handler = Callable[[spacy_pb2_grpc.SpaCyStub, spacy_pb2.Request], spacy_pb2.Reply]


def call(host: str, port: int, sentence: str, handler: Handler):
    with grpc.insecure_channel(f'{host}:{port}') as channel:
        client = spacy_pb2_grpc.SpaCyStub(channel)
        request = spacy_pb2.Request(sentence=sentence)
        reply = handler(client, request)
        rows = [
            [
                token.text,
                token.tag,
                token.lemma,
                token.entity,
                token.index,
                token.length
            ] for token in reply.tokens
        ]

        print(tabulate(rows, headers=["Text", "Tag", "Lemma", "Entity", "Index", "Length"]))


@click.group()
def cli():
    pass


@cli.command()
@click.argument('host', type=str)
@click.argument('sentence', type=str)
@click.option(
    '--port',
    type=int,
    default=DEFAULT_PORT,
    show_default=True,
)
def tag(host: str, sentence: str, port: int) -> None:
    call(host, port, sentence,
         lambda client, request: client.Tag(request))


@cli.command()
@click.argument('host', type=str)
@click.argument('sentence', type=str)
@click.option(
    '--port',
    type=int,
    default=DEFAULT_PORT,
    show_default=True,
)
def ner(host: str, sentence: str, port: int) -> None:
    call(host, port, sentence,
         lambda client, request: client.NER(request))


if __name__ == '__main__':
    cli()
