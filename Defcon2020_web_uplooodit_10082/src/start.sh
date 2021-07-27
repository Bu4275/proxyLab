gunicorn --keep-alive 10 -k gevent --bind 127.0.0.1:8080 -w 20 backend:app --daemon
nohup python bot.py &
nohup python bot_clean.py &
./haproxy -f haproxy.cfg
