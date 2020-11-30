
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from random import random
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello from' + str(random())

if __name__ == "__main__":
    print(random())
