#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Classification using KNN</font></b></h1></center>

# ### Imports 

# In[2]:


import pandas as pd
import numpy as np
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# ### Load Wine Dataset

# In[3]:


wine = datasets.load_wine()


# In[4]:


df = pd.DataFrame(wine.data, columns=wine.feature_names)
df.head()


#  The type of wine, which needs to be predicted based on features above, are in **wine.target**

# In[5]:


wine.target


# ###  Normalizing

# In[6]:


ss = StandardScaler()
transformed = ss.fit_transform(df)
df = pd.DataFrame(transformed,columns=wine.feature_names)
df.head()


# ### Splitting in train and test

# In[7]:


train_data, test_data, train_target, test_target = train_test_split(df,wine.target, test_size=0.20)


# In[8]:


train_data.head()


# ### Apply KNN

# In[10]:


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_data, train_target)


# In[11]:


pred = knn.predict(test_data)
pred


# ### Check Accuracy 

# 1. Manually

# In[12]:


accuracy = np.where(pred == test_target,1,0).sum()/len(test_data)
accuracy


# 2. Using Scikit functions

# In[13]:


metrics.accuracy_score(test_target, pred)

