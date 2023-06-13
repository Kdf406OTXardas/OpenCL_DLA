import pyopencl as cl
import pyopencl.array as cl_array
from pycuda.elementwise import ElementwiseKernel 
import numpy as np


platform = cl.get_platforms()[1]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)


TARGET_POROSITY = 10
FIELD_SIZE = 51
TARGET_PORE_CELLS = TARGET_POROSITY / 100 * FIELD_SIZE * FIELD_SIZE
field_test = np.zeros((FIELD_SIZE + 2 ,FIELD_SIZE + 2))


mf = cl.mem_flags 
q_opencl = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=field_test)
output_opencl = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, field_test.nbytes)

program = cl.Program(context, """ 
__kernel void vectorSum(__global const int *a_g, __global int *res_g) { 
  int gid = get_global_id(0); 
  res_g[gid] = a_g[gid]; 
} 
""").build()
