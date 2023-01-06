FROM python:3.11-slim

LABEL maintainer="saka2jp <saka2jp@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy
