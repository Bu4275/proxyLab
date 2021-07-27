### Nginx + Tomcat

Try to access http://backend:8080/admin/flag


### Usage

Run
```
docker-compose up
```

Go http://127.0.0.1:8083/


### Hint
Nginx default.conf
```
location /admin/ {
    deny all;
    return 403;
}

location / {
    proxy_pass	http://backend;
}
```