from flask import Flask
from flask import request
from flask import escape
import re
import inspect

app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return 'nginx+flask with gunicorn\n' + escape(path) + '\n' + str(request.headers)

@app.route('/admin/flag')
def flag():
    return 'flag'