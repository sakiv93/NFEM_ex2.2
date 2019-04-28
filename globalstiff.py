import numpy as np 
from elstiff import elstiff
from node2ele import node2ele
def globalstiff(length_of_bar,youngs_modulus,area,number_of_elements):
    length_of_element=length_of_bar/number_of_elements
    #print(length_of_element)
    globalstiff=np.zeros([number_of_elements+1,number_of_elements+1])
    #print(globalstiff)
    local_stiffness=elstiff(youngs_modulus,area,length_of_element)
    #print(local_stiffness)
    for element_number in range(1,number_of_elements+1):
        assignment_matrix=node2ele((element_number),number_of_elements)
        #print(assignment_matrix)
        globalstiff=globalstiff+np.matmul(np.transpose(assignment_matrix),np.matmul(local_stiffness,assignment_matrix))
    return globalstiff
#globalstiff=globalstiff(1,1,1,2)
#print(globalstiff)


