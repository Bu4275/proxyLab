### Nginx + Tomcat

Try to access http://backend:8080/admin/flag

### Usage

Run
```
sudo docker-compuse up
```

Go http://127.0.0.1:8084/

### Hint

httpd.conf
```
RewriteEngine On
RewriteCond %{REQUEST_URI} .*\.png$
RewriteRule /(.*) http://backend:8080/$1 [P,L]

ProxyPass / http://backend:3000/
ProxyPassReverse / http://backend:3000/

<Directory />
    AllowOverride none
    Require all denied
</Directory>
```