class Object(object):
    _IDGenerator = 0
    def __init__(self):
        self._objId = Object._IDGenerator
        Object._IDGenerator += 1

# class classname(Object):
#     def __init__(self):
#         super().__init__()
#         print(self._objId)

# x = classname()
# y = classname()
# print(x._objId)