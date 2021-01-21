import paddle.fluid as fluid
import numpy as np
import six

# feature_names = ['x1', 'x2', 'x3', 'y']
# feature_num = len(feature_names)
# data = np.fromfile('./python/paddleStudy/ttt.txt', sep=' ')
# data = data.reshape(data.shape[0] // feature_num, feature_num)
# maximums, minimums, avgs = data.max(axis=0), data.min(axis=0), data.sum(axis=0)/data.shape[0]

# # for i in six.moves.range(feature_num-1):
# #     print(i)

# for i in range(feature_num-1):
#     data[:,i] = (data[:,i] - avgs[i]) / (maximums[i] - minimums[i])

# # print(data)

# x = np.random.random(size=(10,1)).astype('float32')
# print(x)

exe = fluid.Executor()

train_program = fluid.Program()
startup_program = fluid.Program()
with fluid.program_guard(train_program, startup_program):
    data = fluid.layers.data(name='X', shape=[1], dtype='float32')
    print("data:", data)
    hidden = fluid.layers.fc(input=data, size=2)
    print("hidden:", hidden)
    loss = fluid.layers.mean(hidden)
    print("loss:", loss)
    fluid.optimizer.SGD(learning_rate=0.01).minimize(loss)

startup_program.random_seed = 1
exe.run(startup_program)

x = np.random.random(size=(10,1)).astype('float32')
loss_data, = exe.run(train_program,feed={'X':x},fetch_list=[hidden.name])
print("loss_data:", loss_data)