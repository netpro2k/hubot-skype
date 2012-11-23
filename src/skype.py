#!/usr/bin/python
import sys
import json
try:
    import Skype4Py
except ImportError, e:
    sys.stderr.write("""
It seems you have not yet installed Skype4Py. Install by running:
sudo easy_install Skype4Py
or
sudo pip install Skype4Py
        """)
    exit(1)


def on_message(message, status):
    if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
        json_string = json.dumps({
            'user': message.Sender.Handle,
            'message': message.Body,
            'room': message.Chat.Name,
        })
        sys.stdout.write(json_string + '\n')
        sys.stdout.flush()

s = Skype4Py.Skype()
s.Attach()
s.OnMessageStatus = on_message

while True:
    line = sys.stdin.readline()
    try:
        decoded = json.loads(line)
        c = s.Chat(decoded['room'])
        c.SendMessage(decoded['message'])
    except:
        continue
