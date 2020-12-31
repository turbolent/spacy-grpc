FROM python:3.7-slim-stretch as base

FROM base as builder

RUN pip install pipenv

WORKDIR /build
COPY Pipfile* /build/

RUN bash -c 'PIPENV_VENV_IN_PROJECT=1 pipenv sync -v'

FROM base as app

WORKDIR /app
COPY --from=builder /build /app/
COPY . /app/

CMD .venv/bin/python -mspacy_grpc
