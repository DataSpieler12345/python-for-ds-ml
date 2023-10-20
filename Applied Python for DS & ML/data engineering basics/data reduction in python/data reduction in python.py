#!/usr/bin/env python
# coding: utf-8

#    ## PCA with Python

# ### Imports

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
from sklearn import datasets


# ### Load Iris Dataset

# In[3]:


iris = datasets.load_iris()


# ### Check dimensions and Preview Dataset

# In[4]:


iris.data.shape


# In[5]:


iris.data[0:5] # first 5 items only


# In[6]:


iris.target.shape


# In[7]:


iris.target


# ## Create a PCA Object

# In[8]:


pca = PCA(n_components=2)


# ### Fit the model with Data

# In[9]:


pca.fit(iris.data)


# In[11]:


transformed = pca.transform(iris.data)


# In[12]:


transformed[0:5] # first 5 rows


# In[13]:


transformed.shape # dimensions of transformed


# In[16]:


plt.scatter(transformed[:,0], transformed[:,1], c=iris.target)
plt.show()


# In[ ]:




