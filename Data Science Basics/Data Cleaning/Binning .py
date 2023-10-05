#!/usr/bin/env python
# coding: utf-8

# ### Binning 

# #### using pandas.cut

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#Discretize into three equal-sized bins.
pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)


# In[3]:


#Whether to return the bins or not. 
#Useful when bins is provided as a scalar

pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, retbins=True)


# In[4]:


#assign bins specific labels
pd.cut(np.array([1, 7, 5, 4, 6, 3]),
       3, labels=["bad", "medium", "good"])


# In[5]:


#Passing a Series as an input returns a Series with categorical dtype
s = pd.Series(np.array([2, 4, 6, 8, 10]),index=['a', 'b', 'c', 'd', 'e'])
pd.cut(s, 3)

