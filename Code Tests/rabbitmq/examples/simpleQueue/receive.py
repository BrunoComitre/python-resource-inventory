import sys
sys.path.append("../../src")

from rabbit import builder

server = {
    'host': 'localhost',
    'port': 5672,
    'user': 'rabbitadmin',
    'pass': 'secret',
}

def onData(data):
    print data['aaa']

builder.queue('queue.backend', server).receive(onData)
