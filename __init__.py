#!/usr/bin/python3

from flask import (Flask, render_template, redirect, url_for, session, request,
                   flash)

app = Flask(__name__)


@app.route("/calendar")
def hello():
    return render_template('schedule_form.html')


if __name__ == "__main__":
    app.run()
