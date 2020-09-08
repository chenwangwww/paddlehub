import paddle.fluid as fluid
import numpy

a = fluid.data(name="a", shape=[1],dtype='float32')
b = fluid.data(name="b", shape=[1],dtype='float32')
print(a)
result = fluid.layers.elementwise_add(a,b)
cpu = fluid.core.CPUPlace()
exe = fluid.Executor(cpu)
exe.run(fluid.default_startup_program())

x = numpy.array([5]).astype("float32")
y = numpy.array([7]).astype("float32")

outs = exe.run(
    feed={'a':x, 'b':y},
    fetch_list=[result]
)

print(outs)