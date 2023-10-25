#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Anomaly Detection</font></b></h1></center>

# ## Imports

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Load dataset

# In[2]:


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


# In[11]:


df


# ## Create a Box Plot 

# In[3]:


df.boxplot(figsize=(15, 9))


# In[5]:


df.describe()


# In[6]:


Q1 = df["sepal width (cm)"].quantile(0.25)
Q3 = df["sepal width (cm)"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# ## Upper Limit Outliers

# In[7]:


ub = Q3 + 1.5*IQR
ub


# ### look at the outliers

# In[8]:


df[df["sepal width (cm)"] > ub]


# In[9]:


df2 = df[df["sepal width (cm)"] < ub]
df2.shape


# ## Lower Limit Outliers

# In[10]:


lb = Q1 - 1.5*IQR
df2 = df2[df2["sepal width (cm)"] > lb]
df2.shape


# In[12]:


df2.boxplot(figsize=(15, 9))

