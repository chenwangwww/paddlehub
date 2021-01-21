import paddle
import paddle.fluid as fluid
import numpy as np

# a = fluid.create_lod_tensor(np.array([[1.1], [2.2], [3.3], [4.4]]).astype('float32'), [[1,3]], fluid.CPUPlace())
# print('a:', a)
# def lodtensor_to_tensor(lod_tensor):
#     lod = lod_tensor.lod()
#     print('lod:', lod)
#     array = np.array(lod_tensor)
#     print('array:', array)
#     new_array = []
#     for i in range(len(lod[0]) - 1):
#         new_array.append(array[lod[0][i]:lod[0][i+1]])
#     return new_array

# new_array = lodtensor_to_tensor(a)
# print(new_array)

# x = fluid.layers.data(name='x', shape=[None, 1], dtype='float32', lod_level=1)
# print(x)
# y = fluid.layers.data(name='y', shape=[1], dtype='float32', lod_level=2)
# print(y)

# y_d = fluid.create_lod_tensor(np.array([[1.1],[1.1],[1.1],[1.1],[1.1],[1.1]]).astype('float32'), [[1,3], [2,1,2,1]], fluid.CPUPlace())
# print(y_d)

def train_mapper(sample):
    data, label = sample
    data = [int(data) for data in data.split(',')]
    return data, int(label)

def train_reader():
    def reader():
        with open("./paddleStudy/ttt.txt", 'r') as f:
            lines = f.readlines()
            # np.random.shuffle(lines)
            for line in lines:
                data, label = line.split(' ')
                yield data, label
    return paddle.reader.xmap_readers(train_mapper, reader, 1, 1024)

train_rdr = paddle.batch(reader=train_reader(), batch_size=2)

words = fluid.layers.data(name='words', shape=[1], dtype='int64', lod_level=1)
label = fluid.layers.data(name='label', shape=[1], dtype='int64')

place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

feeder = fluid.DataFeeder(place = place, feed_list=[words, label])

for batch_id, data in enumerate(train_rdr()):
    info = exe.run(feed=feeder.feed(data), fetch_list=[words, label], return_numpy=False)
    print(info[0], info[1])