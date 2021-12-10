from flask import Flask

from tasks import test_task


app = Flask(__name__)


@app.route("/test")
def test_page():
    test_task.delay()
    return "OK"
