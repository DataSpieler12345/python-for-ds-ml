import numpy as np
n, p = [int(x) for x in
input().split()]
list = []
for i in range(n):
   list.append(input().split())
print(np.array(list).astype(np.float16).mean(axis=1).round(2))