import numpy as np

# x = numpy.random.random(size=(10, 1)).astype('float32')
# print(x.data)

# for i in range(1,10):
#     print(i)

# class Test:
#     enter = 'Enter...'
#     exit = 'Exit...'
#     def __enter__(self):
#         print(Test.enter)
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'exc_type:{exc_type}')
#         print(f'exc_val:{exc_val}')
#         print(f'exc_tb:{exc_tb}')
#         print(Test.exit)
#         # return True

#     def fun(self):
#         print('fun execute!!!')

# with Test() as obj:
#     1/0
#     obj.fun()

# print('eee')

# fo = open("./python/paddleStudy/ttt.txt", "r")
# line = eval(fo.readlines()[0])
# print(line.keys())
# print(fo.readlines()[1])
# print(line.keys())
    
# arr = numpy.array([1,2,3,4,5,6]).reshape(2,3)
# print(arr)

# data_X = [[6], [7], [8], [9], [11], [12], [13], [17], [18], [19], [20]]
# data_Y = [[1,0,0], [1,0,0], [1,0,0], [1,0,0], [0,1,0], [0,1,0], [0,1,0], [0,0,1], [0,0,1], [0,0,1], [0,0,1]]

# for x_, y_ in zip(data_X, data_Y):
#     x_ = np.array(x_).reshape(1,1).astype('float32')
#     y_ = np.array(y_).reshape(1,3).astype('int64')
#     print("data:", x_, y_)

# x = np.array([1,4,3,-1,6,9])
# print(x.argsort())

# data_X = [[1], [2], [3], [5], [10]]
# data_Y = [[13], [23], [33], [53], [103]]
# zipped = zip(data_X, data_Y)
# for x in zipped:
#     print(x)

# line = 'andnr'
# s = line.replace('n', 's', 1)
# v = line.replace('n', '_!_', 1)
# print(s)
# print(v)

# lis = [['a',1],['b',2],['a',3]]
# dic = dict(lis)
# print(dic)

# with open('./python/paddleStudy/ttt.txt', 'r', encoding='utf-8') as f:
#     dict_txt = eval(f.readlines()[0])
#     print(dict_txt)

# a = [1,2,3]
# b = a[:-1]
# print(b)

# a = [[[1.1]], [[2.2], [3.3], [4.4]]]
# print(a)
# b = np.array(a)
# print(b)
# print(b.shape)

# with open("./python/paddleStudy/ttt.txt", 'r') as f:
#     lines = f.readlines()
#     # np.random.shuffle(lines)
#     for line in lines:
#         data = line.split(' ')
#         print(data)

# print([0] * 10)

data = np.array([[[2,3,2],[1,2,4]]])
lab = np.argsort(data)[0]
print(lab)