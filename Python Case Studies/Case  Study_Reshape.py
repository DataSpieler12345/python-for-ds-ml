r = int(input())
lst = [float(x) for x in 
input().split()]

import numpy as np
arr = np.arry(lst)
arr = arr.reshape(r,int(len(lst)/r))
print(arr.round(2))