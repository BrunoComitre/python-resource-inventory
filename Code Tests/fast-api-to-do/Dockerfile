FROM python:3.8.5-slim-buster

# work directory
WORKDIR /usr/app

# Impede o Python grave arquivos pyc no disco(equivale à python -B option)
ENV PYTHONDONWRITEBYCODE 1

# Impede o Python armazene em buffer stdout e stderr(equivale à python -u option)
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/app/requirements.txt

# RUN set -eux \
#     && apk add --no-cache --virtual .build-deps build-base \
#        libressl-dev libffi-dev gcc musl-dev python3-dev \
#     && pip install --upgrade pip setuptools wheel \
#     && pip install -r /usr/app/requirements.txt \
#     && rm -rf /root/.cache/pip

RUN apt-get update \
    && pip install -r /usr/app/requirements.txt

COPY . /usr/app/

CMD gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0
