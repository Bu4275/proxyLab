from flask import Flask
from flask import request
import re
import inspect

app = Flask(__name__)
@app.route('/')
def index():
    html = '''
    Try to access /flag from 127.0.0.1 </br>
    <a href="header">my_header</a> </br>
    <a href="hint">hint</a>'''

    return html

@app.route('/flag')
def flag():

    src_ip = None
    if 'x-forwarded-for' in request.headers:
            src_ip = request.headers['x-forwarded-for']

    if src_ip is None:
        src_ip = request.remote_addr

    if src_ip == '127.0.0.1':
        return open('flag','r').read()
    else:
        return 'IP From %s is forbidden' % src_ip

@app.route('/header')
def header():
    return str(request.headers)

@app.route('/hint')
def hint():

    html = '''
    
    <pre>
# app.py
@app.route('/flag')
def flag():

    src_ip = None
    if 'x-forwarded-for' in request.headers:
            src_ip = request.headers['x-forwarded-for']

    if src_ip is None:
        src_ip = request.remote_addr

    if src_ip == '127.0.0.1':
        return open('flag','r').read()
    else:
        return 'IP From %s is forbidden' % src_ip

    </pre>

    
<pre>
#httpd.conf
RequestHeader unset X-Forwarded-For
</pre>
    '''
    return html