FROM python:latest
LABEL authors="intron014"
LABEL version="1.0.0"
LABEL description="I014 API in a docker container, woah!"

RUN pip install --no-cache-dir pipenv==2023.12.1

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock

RUN set -ex && \
    pipenv install --dev --system --deploy

ADD app app

CMD exec gunicorn app.main:app