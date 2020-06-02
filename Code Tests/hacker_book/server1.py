'''
# SERVER 1
import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(2)

conn, addr = s.accept()
print("[+]  Connected to", addr)
conn.send(b"BAC IS LIFE")
conn.close()
'''

'''
# SERVER 2
import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i = 0

s.bind((host,port))
s.listen(2)

while i < 10:
    conn, addr = s.accept()
    print("[+]  Conexão bem sucedida, ao ",addr)
    conn.send(b"BAC IS LIFE")
    i += 1
    conn.close()
'''

# SERVER 3
import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(1)

conn, addr = s.accept()
print("[+]  Conectado em ",addr)
conn.send(b"Thanks")
conn.close()
