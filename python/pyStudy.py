#!C:\Python38\python3.exe
# -*- coding: UTF-8 -*-

# class A(object):
#     bar = 1
#     def func1(self):
#         print('foo', self.bar)
#     @classmethod
#     def func2(self):
#         print('func2')
#         self.bar += 1
#         # print(self.bar)
#         self().func1()

# A.func2()
# A.func2()

# class Screen(object):
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value

#     @property
#     def resolution(self):
#         return self._width * self._height

# s = Screen()
# s.width, s.height = 10,10
# print(s.resolution)

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopIteration()
#         return self.a

# vv = Fib()
# for a in vv:
#     print(a)

# a = [1,2,3]
# for i in a:
#     print(i)

# for i in range(10):
#     print(i)

# a = list(range(10))
# print(a[1:3])

# foo = [2,18,9,22]
# b = filter(lambda x: x % 3 == 0, foo)
# print(list(b))
# print('------------------')
# a = [x for x in foo if x % 3 == 0]
# print(a)

# a = map(lambda x: x * 2 + 10, foo)
# print(list(a))
# b = [x * 2 + 10 for x in foo]
# print(b)

# reversed
# a = reversed(foo)
# print(list(a))

# g = lambda x: x + 1
# a = lambda x: 1
# b = a(1)
# print(g(3))

# class student(object):
#     def __init__(self, name):
#         self.name = name

#     # def __call__(self):
#     #     print(self.name)

# s = student('mic')
# # s()
# print(callable(s))

# class person(object):
#     PID: 15

# class student(person):
#     def __init__(self):
#         print(person.PID)

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET /HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()

# print(data)

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('sina.html', 'wb') as f:
#     f.write(html)

# str = "this is string example ... "
# str = str.encode('utf-8')
# print(str)
# print(str.decode('utf-8'))
# addr = ('A','b')
# print('Received from %s:%s.' % addr)

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 9999))
# while True:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % addr)
#     s.sendto(b'Hello, %s!' % data, addr)


#客户端
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in [b'michael', b'Tracy']:
#     s.sendto(data, ('127.0.0.1', 9999))
#     print(s.recv(1024).decode('utf-8'))
# s.close()

# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'michael\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()

# def gen():
#     s = yield "hello"
#     print("value: %s" % s)
#     yield s

# g = gen()
# print(next(g))
# print(g.send('world'))

# def consumer():
#     r = 'h'
#     while True:
#         n = yield r
#         if not n:
#             print("1111")
#             return
#         print('consuming %s...' % n)
#         r = '200 ok'

# def produce(c):
#     print(c.send(None))
#     n = 0
#     while n<5:
#         n = n + 1
#         print('producing %s...' % n)
#         r = c.send(n)
#         print('return: %s' % r)
#     c.close()

# c = consumer()
# produce(c)

# def func():
#     yield from "ad"

# for x in func():
#     print(x)

# def func():
#     n = 0
#     while True:
#         s = yield n
#         if s is None:
#             break
#         n += 1
#     return n

# def deligate():
#     result = yield from func()
#     print("the result is : %s" % result)

# def main():
#     g = deligate()
#     print(next(g))
#     for i in range(3):
#         print(g.send(i))
#     try:
#         g.send(None)
#     except StopIteration:
#         print('wwwww')

# if __name__ == '__main__':
#     main()

# import asyncio

# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()

# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# import asyncio
# from aiohttp import web

# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(text=b'<h1>Index</h1>')

# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))

# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

# import aiohttp
# import asyncio

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:
#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# from aiohttp import web

# async def handle(request):
#     name = request.match_info.get('name', "Anonymous")
#     text = "Hello, " + name
#     return web.Response(text = text)

# app = web.Application()
# app.add_routes([web.get('/', handle),
#                 web.get('/{name}', handle)])

# if __name__ == '__main__':
#     web.run_app(app)

# with open(r'./python/Role.py', 'r') as f:
#     print("eeee")

class Test(object):
    enter = 'Enter...'
    exit = 'Exit...'
    def __enter__(self):
        print(Test.enter)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Test.exit)

    def fun(self):
        print('fun execute!!!')

test = Test()
enter = type(test).__enter__
enter(test)

# with Test() as obj:
#     obj.fun()

# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                       "AppleWebKit/537.36 (KHTML, like Gecko)"
#                       " Chrome/78.0.3904.108 Safari/537.36"
#     }

# print(headers["User-Agent"])
