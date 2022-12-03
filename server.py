from socket import SOCK_STREAM, AF_INET, socket
import json
import datetime
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-a', default='')
parser.add_argument('-p', default=7777)
args = parser.parse_args()

ENCODING = 'UTF-8'
ADDR = args.a
try:
    PORT = int(args.p)
except ValueError:
    sys.exit('Неверный аргумент. В порт должно передавать число')


def run_server(addr=ADDR, port=PORT):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)
    return sock


def decode_data_from_user(data):
    result = json.loads(data.decode(ENCODING))
    return result


def send_response_to_client(client_, code_status=200):
    time = datetime.datetime.now().timestamp()
    json_answer = {
        "response": f"{code_status}",
        "time": f"{time}",
    }
    print(f'Отправлен ответ: {json_answer}')
    client_.send(json.dumps(json_answer).encode(ENCODING))


def main():
    sock = run_server()
    while True:
        client, addr = sock.accept()
        print('Подключение с адреса: ', addr)
        print('-' * 30)
        data = decode_data_from_user(client.recv(100000))
        print(f'Получены данные: {data}')
        print('-' * 30)
        send_response_to_client(client)
        client.close()


if __name__ == '__main__':
    main()
