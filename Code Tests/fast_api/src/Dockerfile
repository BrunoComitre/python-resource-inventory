FROM python:3.8.2-alpine

# work directory
WORKDIR /usr/src/app

# Impede o Python grave arquivos pyc no disco (equivale à python -B option)
ENV PYTHONDONWRITEBYCODE 1

# Impede o Python armazene em buffer stdout e stderr (equivale à python -u option)
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
       libressl-dev libffi-dev gcc musl-dev python3-dev \
       postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip  install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /usr/src/app/
