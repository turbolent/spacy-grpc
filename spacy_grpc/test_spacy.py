import grpc
import grpc_testing
import unittest

import spacy

from spacy_grpc import spacy_pb2, spacy_pb2_grpc
from spacy_grpc.__main__ import SpaCy, load_tagging_language


class TestSpaCyService(unittest.TestCase):
    def setUp(self):
        language = 'en_core_web_sm'
        tagging_nlp = load_tagging_language(language)
        ner_nlp = spacy.load(language)

        servicers = {
            spacy_pb2.DESCRIPTOR.services_by_name['SpaCy']: SpaCy(tagging_nlp, ner_nlp)
        }

        self.test_server = grpc_testing.server_from_dictionary(
            servicers,
            grpc_testing.strict_real_time()
        )

    def test_tag(self):
        request = spacy_pb2.Request(sentence="this is a test")

        method = self.test_server.invoke_unary_unary(
            method_descriptor=spacy_pb2.DESCRIPTOR
                .services_by_name['SpaCy']
                .methods_by_name['Tag'],
            invocation_metadata={},
            request=request,
            timeout=1
        )

        response, metadata, code, details = method.termination()

        self.assertEqual(code, grpc.StatusCode.OK)
        self.assertEqual(
            list(response.tokens),
            [
                spacy_pb2.Token(
                    text="this",
                    tag="DT",
                    lemma="this",
                    index=0,
                    length=4
                ),
                spacy_pb2.Token(
                    text="is",
                    tag="VBZ",
                    lemma="be",
                    index=5,
                    length=2
                ),
                spacy_pb2.Token(
                    text="a",
                    tag="DT",
                    lemma="a",
                    index=8,
                    length=1
                ),
                spacy_pb2.Token(
                    text="test",
                    tag="NN",
                    lemma="test",
                    index=10,
                    length=4
                )
            ]
        )


if __name__ == '__main__':
    unittest.main()
