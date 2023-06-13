import pyopencl as cl
import pyopencl.array as cl_array
from pycuda.elementwise import ElementwiseKernel 
import numpy as np


platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
print(f'device {device}')
context = cl.Context([device])
queue = cl.CommandQueue(context)


TARGET_POROSITY = 10
FIELD_SIZE = 2
TARGET_PORE_CELLS = TARGET_POROSITY / 100 * FIELD_SIZE * FIELD_SIZE
field_test = np.zeros((FIELD_SIZE + 2,
                       FIELD_SIZE + 2),
                      dtype=np.uint16)
field_test_2 = np.full_like(field_test,
                            fill_value=0,
                            dtype=np.uint16)
print(field_test_2)


mf = cl.mem_flags 
field_test_cl = cl.Buffer(context,
                             mf.READ_WRITE | mf.COPY_HOST_PTR,
                             hostbuf = field_test)
field_test_cl_2 = cl.Buffer(context,
                             mf.READ_WRITE | mf.COPY_HOST_PTR,
                             hostbuf = field_test_2)

#   res_g[lid_x][lid_y] = a_g[gid_x][gid_y] + 1; 

program = cl.Program(context, """ 
__kernel void testCl(__global const int **a_g,
                     __global int **res_g) { 
  int gid_x = get_global_id(0); 
  int gid_y = get_global_id(1); 
  
  int i, j;
  
  for (i = 0; i < 2; i++){
      for (j = 0; j < 2; j++){
          res_g[i][j] = a_g[i][j] + 1;
      }
  }
    
} 
""").build()

field_test_out = program.testCl(queue, field_test.shape, None, field_test_cl, field_test_cl_2)
# a_1 = 1
# a_2 = 1
# print(f'field_test[{a_1}][{a_2}] = {field_test_out[a_1][a_2]}')
a = field_test_out
print(a)
