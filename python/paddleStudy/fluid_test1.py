import paddle.fluid as fluid
import numpy as np
#线性回归：y=10x+3
test_data = [[100], [567], [32]]

exe = fluid.Executor(place=fluid.CPUPlace())

Program, feed_target_names, fetch_targets = fluid.io.load_inference_model(dirname='./infer_model', executor = exe)
for x_ in test_data:
    x_ = np.array(x_).reshape(1,1).astype('float32')
    out = exe.run(program = Program, feed = {feed_target_names[0]:x_}, fetch_list = fetch_targets)
    print(out[0])