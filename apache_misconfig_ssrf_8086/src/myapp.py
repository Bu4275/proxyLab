from flask import Flask
from flask import request
import re
import inspect

app = Flask(__name__)
@app.route('/')
def index():
    return str(request.headers)

@app.route('/flag')
def flag():
    return open('flag','r').read()

