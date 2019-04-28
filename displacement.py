import numpy as np 
from globalstiff import globalstiff
from force_external import force_external
def displacement(length_of_bar,youngs_modulus,area,number_of_elements,uniformly_distributed_load):
    gs=globalstiff(length_of_bar,youngs_modulus,area,number_of_elements)
    fex=force_external(length_of_bar,youngs_modulus,area,number_of_elements,uniformly_distributed_load)
    print(fex)
    rgs=gs[1:,1:]
    print(rgs)
    rfe=fex[1:]
    print(rfe)
    displacement=np.zeros([number_of_elements+1,1])
    print(displacement)
    displacement[0,0]=0
    displacement[1:]=np.matmul(np.linalg.inv(rgs),rfe)
    return displacement
displacement=displacement(1,1,1,3,1)
print(displacement)
