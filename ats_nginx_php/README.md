### Lab Apache Traffic Server - CVE-2018-8004

There are HTTP Request Smuggling CL.TE and mutiple issues.

Try to access /flag

### Composition
* Reverse Proxy: Apache Traffic Server 7.1.2
* Backend: nginx 1.9.10

### Usage:
Build and run
``` bash
docker-compose up
```

Go http://127.0.0.1:10080/


### Reference
* https://github.com/ZeddYu/HTTP-Smuggling-Lab/blob/master/lab2/ats7.Dockerfile
