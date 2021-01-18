# spacy-grpc

[spaCy](https://github.com/explosion/spaCy) part-of-speech tagging and named entity recognition as a gRPC service

## Usage

- Run the server:

  ```sh
  $ pipenv run python -m spacy_grpc
  ```

- Run the test client:

  ```shell
  $ PYTHONPATH=. pipenv run python spacy_grpc/client.py tag localhost "Hello, world!"
  Text    Tag    Lemma    Entity      Index    Length
  ------  -----  -------  --------  -------  --------
  hello   UH     hello                    0         5
  ,       ,      ,                        5         1
          _SP                             7         1
  world   NN     world                    8         5
  !       .      !                       13         1
  ```
