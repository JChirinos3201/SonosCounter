#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route("/calendar")
def hello():
    return '<button type="button" class="btn btn-primary">Primary</button>'


if __name__ == "__main__":
    app.run()
