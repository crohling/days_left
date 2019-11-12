from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def days_left():
    """Return number of days until 2022, 10, 31."""
    return str((datetime(2020, 10, 31) - datetime.now()).days)
