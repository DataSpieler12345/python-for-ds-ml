n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
   X.append([float(x) for x in input().split()]) 
   
y = [float(x) for x in input().split()]
import numpy as np
coef_mat = np.linalg.lstsq(X ,y, rcond = None)[0].round(2)
print(coef_mat)
   