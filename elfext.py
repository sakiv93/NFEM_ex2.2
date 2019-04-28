import numpy as np
def elfext(uniformly_distributed_load,length_of_element):
    local_force_external=(uniformly_distributed_load/2*length_of_element)*np.array([[1],[1]])
    return local_force_external
#local_force_external=elfext(1,1)
#print(local_force_external)