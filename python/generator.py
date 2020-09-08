import types
from abc import ABC,abstractmethod

# import threading

# def generator_fun():
#     yield 1

# if __name__ == '__main__':
#     print(generator_fun())
#     print(generator_fun().send(None))
#     for i in generator_fun():
#         print(i)

# async def async_fun():
#     return 1

# if __name__ == '__main__':
#     print(async_fun)
#     # print(async_fun().send(None))
#     try:
#         async_fun().send(None)
#     except StopIteration as e:
#         print(e.value)

# async def async_function():
#     return 1
# async def await_coroutine():
#     result = await async_function()
#     print(result)

# run(await_coroutine())

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# async def async_function():
#     return 1

# async def await_coroutine():
#     result = await async_function()
#     print(result)
    
# run(await_coroutine())

# def funA(fn):
#     print("C语言中文网")
#     fn()
#     print("http")
#     return "装饰器"

# @funA
# def funB():
#     print("学习python")

# def funA(fn):
#     def say(*args, **kwargs):
#         fn(*args, **kwargs)
#         return 'chen'
#     return say

# @funA
# def funB(arc):
#     print("c语言:", arc)

# @funA
# def funC(name, arc):
#     print(name,arc)
# print(funB("http"))
# funC("python:", "g")

# class a(ABC):
#     @abstractmethod
#     def writelog(self):
#         pass

# class b(a):
#     def writelog(self):
#         print('i enjoy writing')

# if __name__ == '__main__':
#     c = b()
#     c.writelog()

# class A():
#     @property
#     def pfunc(self):
#         return self.value
#     @pfunc.setter
#     def pfunc(self, value):
#         self.value = value
#     @property
#     def pfunc1(self):
#         return self.value
#     @pfunc1.setter
#     def pfunc1(self, value):
#         self.value = value

# if __name__ == '__main__':
#     A.pfunc = 9
#     A.pfunc1 = "hello"
#     print(A.pfunc)
#     print(A.pfunc1)

# class A():
#     def func(self, x, y):
#         return x * y
#     @classmethod
#     def cfunc(cls, x, y):
#         return x * y

# if __name__ == '__main__':
#     print(A().func(5,5))
#     print(A.cfunc(4,5))

class A():
    @staticmethod
    def sfunc(x,y):
        return x * y

if __name__ == '__main__':
    print(A.sfunc(6,5))