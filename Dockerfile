FROM python:3.10-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONUNBUFFERED=1

ENV APPLICATION_DIR=/srv/app/celery_test
# Install all requirements
COPY requirements.txt $APPLICATION_DIR/
RUN pip install -r $APPLICATION_DIR/requirements.txt

COPY entrypoint.sh celery_entrypoint.sh config.ini wsgi.py $APPLICATION_DIR/

COPY app/ $APPLICATION_DIR/app/
WORKDIR $APPLICATION_DIR
