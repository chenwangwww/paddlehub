import socket
import sys
import threading

class myThread(threading.Thread):
    def __init__(self, name, conn, addr):
        threading.Thread.__init__(self)
        self.setName(name)
        self.conn = conn
        self.addr = addr
    def run(self):
        print("thread " + str(self.addr) + " start!")
        while True:
            data = self.conn.recv(1024)
            if not data:
                self.conn.close()
                break
            print("连接地址: %s, 数据: %s" % (str(self.addr), data.decode()))
            self.conn.send('hello'.encode('utf-8'))
        print("thread " + str(self.addr) + " end!")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''#socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(2)

i = 1
while True:
    print("waiting")
    conn, addr = serversocket.accept()
    thread = myThread("thread-" + str(i), conn, addr)
    thread.start()

# while True:
#     print("waiting")
#     conn, addr = serversocket.accept()
#     print("call")
#     data = conn.recv(1024)
#     print('received:', data)
#     conn.send('hello world 陈'.encode('utf-8'))

# while True:
#     print("www")
#     clientsocket, addr = serversocket.accept()
#     print("连接地址: %s" % str(addr))

    # msg = 'hello world'
    # clientsocket.send(msg.encode('utf-8'))
    # clientsocket.close()
#     while True:
#         data = clientsocket.recv(1024)
#         if not data: 
#             clientsocket.close()
#             break
#         print("连接地址: %s, 数据: %s" % (str(addr), data.decode()))
#         clientsocket.send('hello world'.encode('utf-8'))

# serversocket.close()

