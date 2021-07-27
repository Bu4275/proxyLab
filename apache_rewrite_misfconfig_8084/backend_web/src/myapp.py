from flask import Flask
from flask import request
import re
import inspect

app = Flask(__name__)
@app.route('/')
def index():
    html = '''Try to get http://127.0.0.1:8080/flag.</br>
    <a href="hint">hint</a></br>
    <img src=418.png>'''

    return html

@app.route('/hint')
def hint():

    html = '''
<pre>
# httpd.conf
	RewriteEngine On
	RewriteCond %{REQUEST_URI} .*\.png$
	RewriteRule /(.*) http://backend_res:8080/$1 [P,L]

	ProxyPass / http://backend_web:3000/
	ProxyPassReverse / http://backend_web:3000/

	<Directory />
	    AllowOverride none
	    Require all denied
	</Directory>
</pre
'''
    return html