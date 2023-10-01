#!/usr/bin/env python
# coding: utf-8

# ## Series

# In[1]:


#Import pandas
# A basic series, which can be created is an Empty Serie
import pandas as pd
s = pd.Series()
print(s)


# In[2]:


#Create numpy 1-d array
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)


# In[3]:


#Create a Series from numpy array
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)


# In[4]:


#Create a Series from dictionary
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)


# In[5]:


#Create an empty DataFrame 
df = pd.DataFrame()
print(df)


# In[6]:


#Create a DataFrame from Lists
data = [1,2,3,4,5]
df= pd.DataFrame(data)
print(df)


# In[7]:


#Create a DataFrame from Dict of ndarrays / Lists
data = {'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)


# In[8]:


#Create a DataFrame from Dict of Series 
d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
    'two' : pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)
print(df)


# In[9]:


#Column selection
d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
    'two' : pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)
print(df['one'])


# In[10]:


#column adition 
d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
    'two' : pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series
print("Adding a new column by passing as Series")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print("Adding a new column using the existing columns in DataFrame")
df['four']=df['one']+df['three']

print(df)

