import json
from socket import SOCK_STREAM, AF_INET, socket
import datetime
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-a', default='localhost')
parser.add_argument('-p', default='7777')
args = parser.parse_args()

ENCODING = 'UTF-8'
ADDR = args.a
try:
    PORT = int(args.p)
except ValueError:
    sys.exit('Неверный аргумент. В порт должно передавать число')


def start_connection(addr=ADDR, port=PORT):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))
    return sock


def send_presence_to_server(sock, username='my_name'):
    time = datetime.datetime.now().timestamp()
    message = {
        "action": "presence",
        "time": f"{time}",
        "type": "status",
        "user": {
            "account_name": f'{username}',
            "status": "online"
        }
    }
    sock.send(json.dumps(message).encode(ENCODING))


def decode_answer_from_server(answer):
    result = json.loads(answer.decode(ENCODING))
    return result


def get_answer_from_server(sock):
    data = sock.recv(10000)
    result = decode_answer_from_server(data)
    return result


def main():
    sock = start_connection()
    send_presence_to_server(sock)
    answer = get_answer_from_server(sock)
    print(answer)


if __name__ == '__main__':
    main()
