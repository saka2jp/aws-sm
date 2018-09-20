FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install pipenv && \
    pipenv install --system --dev
