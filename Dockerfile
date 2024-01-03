FROM python:3.11-alpine


ARG run_env=development
ENV env $run_env
#LABEL "channel"=""
#LABEL "creator"=""

WORKDIR ./

VOLUME /allure-results

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN poetry install

CMD pytest -m "$env" -s -v tests_acceptance/* --alluredir=allure-results