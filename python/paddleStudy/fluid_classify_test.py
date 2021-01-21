import paddle.fluid as fluid
import numpy as np

test_data = [[5], [7], [1,1], [1,2], [1,7], [2,0]]

place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

base_shape = [[len(c) for c in test_data]]

# 生成预测数据
tensor_words = fluid.create_lod_tensor(test_data, base_shape, place)

Program, feed_target_names, fetch_targets = fluid.io.load_inference_model(dirname='./infer_classify_model', executor=exe)
# for x_ in test_data:
#     x_ = np.array(x_).reshape(1,1).astype('int64')
#     out = exe.run(program=Program, feed={feed_target_names[0]:x_}, fetch_list=fetch_targets)
#     print(out[0])
out = exe.run(program=Program, feed={feed_target_names[0]:tensor_words}, fetch_list=fetch_targets)

results = [np.argsort(data)[-1] for data in out[0]]
print(results)