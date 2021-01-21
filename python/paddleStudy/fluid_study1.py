import paddle.fluid as fluid
import numpy as np
#线性回归：y=10x+3
data_X = [[1], [2], [3], [5], [10]]
data_Y = [[13], [23], [33], [53], [103]]

x = fluid.layers.data(name='x', shape=[1], dtype='float32')
y = fluid.layers.data(name='y', shape=[1], dtype='float32')

out = fluid.layers.fc(input=x, size=2)

loss = fluid.layers.square_error_cost(input=out, label=y)
avg_loss = fluid.layers.mean(loss)

opt = fluid.optimizer.SGD(learning_rate=0.01)
opt.minimize(avg_loss)

place = fluid.CPUPlace()
start = fluid.default_startup_program()
exe = fluid.Executor(place)
exe.run(start)

for i in range(100):
    for x_, y_ in zip(data_X, data_Y):
        print("before", x_, y_)
        x_ = np.array(x_).reshape(-1,1).astype('float32')
        y_ = np.array(y_).reshape(-1,1).astype('float32')
        print("after", x_, y_)
        info = exe.run(feed={'x':x_, 'y':y_}, fetch_list=[loss, avg_loss, out, y])
    if i%10 == 0:
        print(info[0], info[1], info[2], info[3])

# fluid.io.save_inference_model(dirname='./infer_model', feeded_var_names=['x'], target_vars=[out], executor=exe)