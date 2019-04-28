import numpy as np
def elstiff(youngs_modulus,area,length_of_element):
    local_stiffness=(youngs_modulus*area/length_of_element)*np.array([[1,-1],[-1,1]])
    return local_stiffness
#local_stiffness=elstiff(1,1,1)
#print(local_stiffness)
