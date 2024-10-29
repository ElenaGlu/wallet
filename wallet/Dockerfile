FROM python:3.12

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN python -m pip install --upgrade pip
RUN pip install --upgrade poetry && poetry --version

RUN poetry install