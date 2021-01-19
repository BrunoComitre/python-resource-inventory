FROM python:3.8.2-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/flasknote

COPY ./requirements.txt /usr/flasknote/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /usr/flasknote/requirements.txt

COPY . /usr/flasknote