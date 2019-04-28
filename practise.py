import numpy as np
a=np.array([[1,0,0],[0,1,0]])
b=np.array([[-1,1],[1,-1]])
c=np.matmul(np.transpose(a),b)
print(c)