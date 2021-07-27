import os
from flask import Flask, request, escape, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'GPOST'])
def root():
    if request.method == 'GPOST':
        return 'flag{thi$_sh@u1d_b_denied_by_HAPr0xy}'

    html = '''Try to use "GPOST" verb</br/>
              <a href="/echo">XSS or Get your headers</a></br>
              <a href="/redirect">Open redirect</a>'''
    return html

@app.route('/flag', methods=['GET'])
def flag():
    return 'flag{nothing_here}'


@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        return str(request.form['msg'])
    else:
        return '''<html>
   <body>
      <form action = "/echo" method="post">
         <p>Echo Test:</p>
         <p><input type="text" name="msg" /></p>
         <p><input type="submit" value="submit" /></p>
      </form>   
   </body>
</html>'''

@app.route('/redirect', methods=['GET', 'POST'])
def redirecto():
    return redirect("http://%s" % (request.host), code=302)
