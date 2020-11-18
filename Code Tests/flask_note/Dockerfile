FROM python:3.8.2-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/flasknote

COPY ./requirements.txt /usr/flasknote/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /usr/flasknote/requirements.txt

COPY . /usr/flasknote

EXPOSE 5000
EXPOSE 27017

CMD gunicorn -w 4 main:app --host 0.0.0.0 --port 5000 /bin/bash