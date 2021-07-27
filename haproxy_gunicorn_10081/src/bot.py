import uuid
import requests
import time


data = 'flag{th1s_is_my_secret_content}'
url = 'http://127.0.0.1:8888/files/'

while True:
    uid = str(uuid.uuid4())

    headers = {'X-guid': uid,
               'Content-Type': 'text/plain'}

    res = requests.post(url, headers=headers, data=data)
    print(uid)
    print(res.status_code)
    time.sleep(0.5)

