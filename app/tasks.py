from .celery import app


@app.task(name="test-task")
def test_task():
    print(f"hello from {test_task}")
