import numpy as np
from node2ele import node2ele
from elfext import elfext
def force_external(length_of_bar,youngs_modulus,area,number_of_elements,uniformly_distributed_load):
    length_of_element=length_of_bar/number_of_elements
    force_external=np.zeros([number_of_elements+1,1])
    for element_number in range(1,number_of_elements+1):
        assignment_matrix=node2ele((element_number),number_of_elements)
        ef=elfext(uniformly_distributed_load,length_of_element)
        force_external=force_external+(np.matmul(np.transpose(assignment_matrix),ef))
    return force_external
#force_external=force_external(1,1,1,2,1)
#print(force_external)