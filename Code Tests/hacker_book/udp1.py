'''
# UDP 1
import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host,port))

data, addr = s.recvfrom(1024)

print(b"[*]  Received from ",addr)
print(b"[+]  Obtained ", data)
s.close()
'''

# UDP 2
import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host,port))
s.settimeout(5)

data, addr = s.recvfrom(1024)

print(b"[*]  Received from ",addr)
print(b"[+]  Obtained ", data)
s.close()
