
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from random import random
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello from' + "sema"
@app.route('/homepage')
def oh():
    return render_template("first.html")
if __name__ == "__main__":
    print(random())
