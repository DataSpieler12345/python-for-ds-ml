import numpy as np
import pandas as pd

lst = [float(x) if x != 'nan' else 
       np.NaN for x in input().split()]
arr=np.asarray(lst)
pd=pd.Series(arr)
p=pd.fillna(pd.mean().round(1))
print(p)