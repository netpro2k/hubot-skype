#!/usr/bin/python
import sys
import json
import os
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

if sys.platform.startswith('linux'):
    s = Skype4Py.Skype(Transport=os.environ.get('HUBOT_SKYPE_TRANSPORT', 'x11'))
else:
    s = Skype4Py.Skype()

s.OnMessageStatus = on_message
s.Attach()

while True:
    line = sys.stdin.readline()
    try:
        decoded = json.loads(line)
        c = s.Chat(decoded['room'])
        c.SendMessage(decoded['message'])
    except:
        continue
