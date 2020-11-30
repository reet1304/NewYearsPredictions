# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from random import random

from bot_token import update_route
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from' + "sema"


@app.route('/homepage')
def oh():
    return render_template("first.html")


if __name__ == "__main__":
    print(random())


@app.route(update_route)
def telegram(*args, **kwargs):
    with open('file.abra.cadabra', 'w') as f:
        f.write(str(args or "no args"))