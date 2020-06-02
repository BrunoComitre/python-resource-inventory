import sys
sys.path.append("../../src")

from rabbit import builder

server = {
    'host': 'localhost',
    'port': 5672,
    'user': 'rabbitadmin',
    'pass': 'secret',
}

print(builder.rpc('rpc.hello', server).call("Gonzalo", "Ayuso"))
