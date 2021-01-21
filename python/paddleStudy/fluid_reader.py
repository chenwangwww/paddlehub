import paddle.fluid as fluid

place = fluid.CPUPlace()
exe = fluid.Executor(place)

def reader():
    data = [i for i in range(10)]
    for sam in data:
        yield sam

batch_size = 10
reader = fluid.io.shuffle(reader, buf_size = 5)
train_reader = fluid.io.batch(reader, batch_size = batch_size)

for i, data in enumerate(train_reader()):
    print(i, len(data), data)