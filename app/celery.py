from configparser import ConfigParser
from pathlib import Path

from celery import Celery


def create_celery_app() -> Celery:
    """Method to create Celery app with configuration from the .ini file,
    and to configure the schedules
    """
    config = ConfigParser()
    config_path = Path("config.ini")
    config.read(config_path)
    # configure celery
    celery_app = Celery("test-celery")
    celery_section = config["celery"]
    celery_app.config_from_object(celery_section)
    celery_app.autodiscover_tasks(["app"])
    # define beat schedules
    celery_app.conf.beat_schedule = {
        "test-task-schedule": {"task": "test-task", "schedule": 30.0}
    }
    return celery_app


app = create_celery_app()
