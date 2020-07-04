FROM python:3.7-slim-buster

ENV WORK_DIR=/usr/src/app

RUN pip install pipenv

COPY ./src ${WORK_DIR}/src
COPY ./Pipfile ${WORK_DIR}
COPY ./Pipfile.lock ${WORK_DIR}

WORKDIR ${WORK_DIR}

RUN pipenv install --system

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
