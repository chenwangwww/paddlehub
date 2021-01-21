import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "121.4.148.42"#socket.gethostname()
port = 9999
client.connect((host, port))
# msg = client.recv(1024)
# client.close()
# print(msg.decode('utf-8'))

while True:
    data = input(">>> ")
    if not data: break
    client.send(bytes(data, encoding='utf-8'))
    recv_data = client.recv(1024)
    if not recv_data: break
    print(recv_data.decode())

client.close()