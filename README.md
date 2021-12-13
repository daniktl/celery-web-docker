# Flask-Celery-Docker integration

## Why

This repository contains starter pack for the Flask web application integration with the Celery. 

It shows how to configure a basic Docker setup to manage your web app along with the Celery worker and beat scheduler.

## What

As for now - it contain the basic setup with:

* Simple Flask web app with the test endpoint.
* Celery app with the one test worker.
* `.ini` configuration file. You could use the configuration file you need, this example shows how the `.ini` configuration could be parsed to configure the Celery app.

## How

To run this app make sure you have docker and docker-compose [installed](https://docs.docker.com/engine/install/).

Then just run the `docker-compose up` and the project will be started.

## Future

There're couple of things to be added to create a real web application example:

* Use the Flask web app context for the Celery worker to manage the DB.
* Add tests to ensure the code is working and stable.
