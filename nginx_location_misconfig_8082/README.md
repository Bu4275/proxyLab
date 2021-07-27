### Nginx

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
location = / {
    return 301 $scheme://$http_host/docs;
}

location /docs {
    proxy_pass	http://backend:8080/docs/;
}
```