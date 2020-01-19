#!/usr/bin/python3

from flask import (Flask, render_template, redirect, url_for, session, request,
                   flash)

app = Flask(__name__)


@app.route("/book/head")
def get_head():
    return render_template('book_head.html')


@app.route("/book/body")
def get_body():
    return render_template('book_body.html')


@app.route("/book/scripts")
def get_scripts():
    return render_template('book_scripts.html')


if __name__ == "__main__":
    app.run()
