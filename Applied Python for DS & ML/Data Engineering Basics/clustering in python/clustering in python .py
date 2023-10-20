#!/usr/bin/env python
# coding: utf-8

# ### Clustering in Python 

# ### Imports

# In[2]:


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


# ### Load iris dataset

# In[3]:


iris = load_iris()


# ### Preview Data

# In[4]:


iris.data


# ### Data Description

# #### species code

# In[5]:


iris.target #  are species


# #### species names

# In[6]:


iris.target_names


# ## Calculate K-Means

# ### Create KMeans Object

# In[7]:


km = KMeans(n_clusters = 3)


# ### Compute k-means clustering 

# In[9]:


import warnings
warnings.filterwarnings("ignore")


# In[13]:


model = km.fit(iris.data)


# ### Review labels of each point

# In[14]:


model.labels_


# ### Coordinates of cluster centers

# In[15]:


model.cluster_centers_


# ### Compute a cross tabulation of species and cluster labels

# In[16]:


pd.crosstab(iris.target, model.labels_)


# ### Scatter plot of petal width vs petal height

# In[18]:


plt.scatter(iris.data[:,2], iris.data[:,3], c=iris.target)

