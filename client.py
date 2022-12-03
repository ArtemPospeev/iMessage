from socket import SOCK_STREAM, AF_INET, socket

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 8002))

msg = 'Hi, server!'
sock.send(msg.encode('utf-8'))

data = sock.recv(1000000)
print(f'Message from server {data.decode("utf-8")}')
