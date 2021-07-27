from flask import Flask
from flask import request
import re
import inspect

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    Try to access /admin/flag </br>
    <a href="hint">hint</a>'''

    return html
@app.route('/admin/flag')
def flag():
    return open('flag','r').read()

@app.route('/hint')
def hint():

    html = '''
<pre>
# httpd.conf
RewriteEngine On
RewriteCond %{REQUEST_URI} ^/admin/flag$ [NC]
RewriteRule ^.*$ - [F,L]

ProxyPreserveHost On
ProxyPass / http://127.0.0.1:3000/
ProxyPassReverse / http://127.0.0.1:3000/
'''
    return html