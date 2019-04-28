import numpy as np 
def node2ele(element_number,number_of_elements):
    assignment_matrix=np.zeros([2,number_of_elements+1])
    assignment_matrix[0,element_number-1]=1
    assignment_matrix[1,element_number]=1
    return assignment_matrix
#assignment_matrix=node2ele(1,2)
#print(assignment_matrix)