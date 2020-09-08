from collections.abc import Iterable, Iterator
from functools import reduce
import functools

# def fun(name, *args):
#     print('你好：', name)
#     for i in args:
#         print('你的宠物有:', i)

# fun("Geek", "dog", "cat")

# def fun2(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} 喜欢 {1}".format(key, value))

# fun2(Geek = 'cat', cat = 'box')

# def foo(*args, **kwarg):
#     for item in args:
#         print(item)
#     # for k,v in kwarg.items():
#     #     print (k,v)
#     print (30*'=')

# if __name__ == '__main__':
#     v = (1,2,4)
#     v2 = [11,15,24]
#     d = {'a':1, 'b':12}
#     foo(v,d)
    # foo(*v, **d)
    # foo(v2,d)
    # foo(*v2, **d)

# def foo2(*args, **kwarg):
#     print (args)
# d = {'a':1, 'b':3}
# foo2(*d)
# foo2(**d)

# L = [x*x for x in range(10)]
# print(L)

# g = (x*x for x in range(10))
# # print(g)
# # print(next(g))
# for n in g:
#     print(n)

# def fib(max):
#     n,a,b = 0,1,1
#     while n<max:
#         yield b
#         a,b = b, a+b
#         n = n+1
#     return 'done'
# f = fib(6)
# for n in f:
#     print(n)

# print(isinstance([], Iterable))
# print(isinstance([], Iterator))

# def f(x):
#     return x*x

# r = map(f, [1,2,3,4])
# print(list(r))

# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

# def fn(x,y):
#     return x*10 + y
# s = reduce(fn, [1,3,5,7,9])
# print(s)

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# print(str2int('123'))

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# print(list(map(char2num, '13579')))

# def not_empty(s):
#     return s and s.strip()
# li = list(filter(not_empty, ['a', '', 'B', None, '  ']))
# print(li)

# def not_empty(s):
#     print(s)
#     re = s and s.strip()
#     print(re)
# not_empty('A')
# not_empty('  A   ')

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f1,f2,f3 = count()
# print(f1(), f2(), f3())

# f = lambda x: x*x
# print(f(5))

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('tt')
# def now():
#     print('2015-03-23')

# now()

# print('𠮷')

# import mod

# mod._test()

# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# class Dock(object):
#     def run(self):
#         print('Dock is running...')

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Dock())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))