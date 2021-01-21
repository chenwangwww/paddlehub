import paddle
import paddle.fluid as fluid
import numpy as np
#分类

def train_mapper(sample):
    data, label = sample
    data = [int(data) for data in data.split(',')]
    return data, int(label)

def train_reader():
    def reader():
        with open("./paddleStudy/ttt.txt", 'r') as f:
            lines = f.readlines()
            np.random.shuffle(lines)
            for line in lines:
                data, label = line.split(' ')
                yield data, label
    return paddle.reader.xmap_readers(train_mapper, reader, 1, 1024)

train_rdr = paddle.batch(reader=train_reader(), batch_size=10)

x = fluid.layers.data(name='x', shape=[1], dtype='int64', lod_level=1)
y = fluid.layers.data(name='y', shape=[1], dtype='int64')

# out = fluid.layers.fc(input=x, size=3, act='softmax')
# out = fluid.layers.fc(input=fluid.layers.fc(input=x, size=100, act='relu'), size=3, act='softmax')
emb = fluid.layers.embedding(input=x,
                                 size=[1024, 128],
                                 param_attr=fluid.ParamAttr(learning_rate=30.0))

# bi-lstm layer
fc0 = fluid.layers.fc(input=emb, size=128 * 4)

rfc0 = fluid.layers.fc(input=emb, size=128 * 4)

lstm_h, c = fluid.layers.dynamic_lstm(input=fc0, size=128 * 4, is_reverse=False)

rlstm_h, c = fluid.layers.dynamic_lstm(input=rfc0, size=128 * 4, is_reverse=True)

# extract last layer
lstm_last = fluid.layers.sequence_last_step(input=lstm_h)
rlstm_last = fluid.layers.sequence_last_step(input=rlstm_h)

# concat layer
lstm_concat = fluid.layers.concat(input=[lstm_last, rlstm_last], axis=1)

# full connect layer
fc1 = fluid.layers.fc(input=lstm_concat, size=96, act='tanh')
# softmax layer
out = fluid.layers.fc(input=fc1, size=3, act='softmax')

loss = fluid.layers.cross_entropy(input=out, label=y)
avg_loss = fluid.layers.mean(loss)

optimizer = fluid.optimizer.AdagradOptimizer(learning_rate=0.002)
opt = optimizer.minimize(avg_loss)

place = fluid.CPUPlace()
feeder = fluid.DataFeeder(place = place, feed_list=[x, y])
start = fluid.default_startup_program()
exe = fluid.Executor(place)
exe.run(start)

for i in range(100):
    for batch_id, data in enumerate(train_rdr()):
        info = exe.run(feed=feeder.feed(data), fetch_list=[out, x, y, loss], return_numpy=False)
        if i == 99:
            print(info[0], info[1], info[2], info[3])

fluid.io.save_inference_model(dirname='./infer_classify_model', feeded_var_names=['x'], target_vars=[out], executor=exe)