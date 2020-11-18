import socket

host = "10.0.200.113"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(s.sendto(b"Hello All",(host,port)))
s.close()
