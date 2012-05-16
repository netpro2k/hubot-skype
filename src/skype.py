#!/usr/bin/python
import Skype4Py
import sys
import json


def on_message(message, status):
    if status == Skype4Py.cmsReceived:
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
