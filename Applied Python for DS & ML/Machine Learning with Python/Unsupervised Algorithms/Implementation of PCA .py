#!/usr/bin/env python
# coding: utf-8

# ### Implementation of PCA

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# #### load the data 

# In[4]:


X = pd.read_csv('data/X.csv')


# In[5]:


print(X.shape)


# In[6]:


X


# #### Import Normalizer

# In[8]:


from sklearn.preprocessing import Normalizer
X = Normalizer().fit_transform(X)


# #### Import PCA

# In[9]:


from sklearn.decomposition import PCA
pca = PCA()
pca.fit(X)
reduced = pca.transform(X)
reduced.shape


# In[10]:


reduced


# In[12]:


comp = pca.components_
print(comp.shape)
print(pca.components_)


# #### pca.explained_variance_ratio_)

# In[13]:


print(pca.explained_variance_ratio_)


# #### pca.explained_variance_ratio_.cumsum()

# In[14]:


print(pca.explained_variance_ratio_.cumsum())


# #### (pca.explained_variance_ratio_[0])
# 
# #### (pca.explained_variance_ratio_[1])
# 
# #### (pca.explained_variance_ratio_[2]

# In[16]:


print(pca.explained_variance_ratio_[0])
print(pca.explained_variance_ratio_[1])
print(pca.explained_variance_ratio_[2])


# #### fit

# In[17]:


pca = PCA().fit(X)
plt.plot(pca.explained_variance_ratio_.cumsum())
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');


# #### n_components  argument

# In[18]:


pca = PCA(n_components = .95, svd_solver = 'full')
pca.fit(X)
reduced = pca.transform(X)
reduced.shape


# In[20]:


print(pca.explained_variance_ratio_[0])

