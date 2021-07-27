import os
import re

from flask import Flask, abort, request, send_from_directory

import store

GUID_RE = re.compile(
    r"\A[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\Z"
)

app = Flask(__name__, static_url_path='')
app.config["MAX_CONTENT_LENGTH"] = 512

# filestore = store.S3Store()
# Uncomment the following line for simpler local testing of this service
filestore = store.LocalStore()


@app.route("/files/", methods=["POST"])
def add_file():
    if request.headers.get("Content-Type") != "text/plain":
        abort(422)

    guid = request.headers.get("X-guid", "")
    if not GUID_RE.match(guid):
        abort(422)

    filestore.save(guid, request.data)
    return "", 201


@app.route("/files/<guid>", methods=["GET"])
def get_file(guid):
    if not GUID_RE.match(guid):
        abort(422)

    try:
        return filestore.read(guid), {"Content-Type": "text/plain"}
    except store.NotFound:
        abort(404)


@app.route("/", methods=["GET"])
def root():
    
    content = '''<a href="https://raw.githubusercontent.com/m3ssap0/CTF-Writeups/master/DEF%20CON%20CTF%20Qualifier%202020/uploooadit/app.py">app.py</a></br>
<a href="https://raw.githubusercontent.com/m3ssap0/CTF-Writeups/master/DEF%20CON%20CTF%20Qualifier%202020/uploooadit/store.py">store.py</a></br></br></br>
Reference:</br>
<a href="https://ctftime.org/task/11590">Defcon CTF 2020 uplooodit</a></br>
<a href="https://nathandavison.com/blog/haproxy-http-request-smuggling">HAProxy HTTP request smuggling</a></br>
'''
    return content, 200

@app.route('/source/<path:path>')
def send_file(path):
    return send_from_directory('source', path)
