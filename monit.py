import requests
import json
import os
import sys
import pdb
import time
import threading

class Monit:

self.auth = "[PUT YOUR PUSHBULLET TOKEN HERE]"

    def __init__(self, ip):
        self.ip = ip

        thread = threading.Thread(target=self.logic, args=())
        thread.daemon = True # Daemonize thread
        thread.start() 
    def send(self):

        remote = "https://api.pushbullet.com/v2/pushes"

        data = {"type": "note", "title": "Server Down!", "body": "Server "+self.ip+ " cannot be reached."}

        session = requests.Session()
        session.auth = (self.auth, "")
        session.headers.update({'Content-Type': 'application/json'})

        pureturn = session.post(remote, data=json.dumps(data))

        return pureturn.reason

    def ping(self):

        response = os.system("ping -c 2 " + self.ip)

        if response == 0:
            return 0
        else:
            return 1
    def logic(self):
        res = self.ping()
        if res == 1:
            self.send()
            time.sleep(3600)
            self.logic()
        else:
            time.sleep(300)
            self.logic()

monit = Monit(sys.argv[1])
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye') 
