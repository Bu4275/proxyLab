import time
import os, re, os.path



temp_dir = "/tmp/uploooodit"
while True:
    if os.path.isdir(temp_dir):
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
    time.sleep(30)
