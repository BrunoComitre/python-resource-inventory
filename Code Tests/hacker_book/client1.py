'''
# CLIENT 1
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.200.113"
port = 12345

s.connect((host, port))
print('[*]  ', s.recv(1024))
s.send(b"Hello SERVER")
s.close()
'''

import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

buf = bytearray(b"-" * 30) # buffer criado
print(b"[*]  Numero de bytes ",s.recv_into(buf))
print(buf)
s.close
