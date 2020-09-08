import paddle.fluid as fluid
import numpy as np

a = fluid.create_lod_tensor(np.array([[1],[1],[1],
                                  [1],[1],
                                  [1],[1],[1],[1],
                                  [1],
                                  [1],[1],
                                  [1],[1],[1]]).astype('int64'),
                                  [[3,1,2], [3,2,4,1,2,3]],
                                  fluid.CPUPlace())

print(len(a.recursive_sequence_lengths()))

print(a.recursive_sequence_lengths())
print(a)