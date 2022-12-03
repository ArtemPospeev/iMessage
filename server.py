from socket import SOCK_STREAM, AF_INET, socket
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8002))
sock.listen(5)

while True:
    client, addr = sock.accept()
    data = client.recv(1000000).decode("utf-8")
    print(f'Response accepted from: {addr}')
    print(f'Data from client: {data}')
    msg = 'Hi, client!'
    client.send(msg.encode('utf-8'))
    client.close()
