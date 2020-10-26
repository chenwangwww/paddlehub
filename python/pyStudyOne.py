# class MyNumbers(object):
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# print('''line1\n
#         line2
# line3''')

# def foo(x):
#     print(locals())
# foo(1)

# print(issubclass(int, object))

def logger(func):
    def inner(*args, **kwargs):
        print("arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x * y

@logger
def foo2():
    return 2
foo1(5,4)
foo1(1)
foo1(3,y=5)
foo2()