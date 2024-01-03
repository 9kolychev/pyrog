FROM python:3.11-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash && \
    apk add --no-cache curl

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s ~/.local/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry install --no-interaction --no-ansi

COPY . /code

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD pytest -m "$env" -s -v tests_acceptance/* --alluredir=allure-results