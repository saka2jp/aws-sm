FROM python:3.7-slim

LABEL maintainer="jumpyoshim <jumpyoshim@gmail.com>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy
