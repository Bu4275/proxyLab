from flask import Flask
from flask import request
from flask import escape
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'GPOST'])
def index():

    return 'Try to access /flag'

@app.route("/flag")
def flag():
    return "flag{ACL_is_n0t_always_u$efu1}"
