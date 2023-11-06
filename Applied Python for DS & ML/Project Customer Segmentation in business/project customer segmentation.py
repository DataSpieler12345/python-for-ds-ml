#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Project List</font></b></h1></center>

# <center><h1><b><font size="2">Customer Segmentation is a popular application of unsupervised learning. Using clustering, companies identify segments of customers to target the potential user base. They divide customers into groups according to common characteristics like gender, age, interests, and spending habits so they can market to each group effectively. By understanding this, you can better understand how to market and serve them. This is similar and related but slightly different from the UX methodology of creating user personas: creating your ideal customers, their pain points, a defining quote, and so on, to understand their perspective.</font></b></h1></center>
# 
# #### Tools: Python
# 
# **Techniques**: K-means clustering, Matplotlib, seaborn
# 
# **Data-set**: Customers.csv dataset

# ### Imports

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


# #### import the data 

# In[6]:


df = pd.read_csv("./data/Customers.csv")


# In[9]:


df.head(10)


# In[10]:


#last 5 rows
df.tail(10)


# In[11]:


#shape of the dataset
df.shape


# In[12]:


#info
df.info()


# ### Unsupervised Learning approach

# In[13]:


#create a separate data frame
X = df.iloc[:, [3,4]].values


# In[14]:


X


# ### KMeans algorithm

# ### finding the optimal values using the elbow method

# In[22]:


from sklearn.cluster import KMeans
wcss = []


# In[23]:


#iteration
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init='k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) #seg data


# In[24]:


#wcss values
wcss


# In[25]:


#display the elbow plot
plt.plot(range(1,11), wcss)
plt.title("The elbow method")
plt.xlabel("No. of clusters")
plt.ylabel("WCSS Values")
plt.show()


# ### Training a model using unsupervised learning K-Means algorithm
# 

# #### Initializing our K-Means Model with selected optimal No. of clusters

# In[35]:


# the model
kmeansmodel = KMeans(n_clusters = 5, init = 'k-means++', random_state=0)


# In[36]:


# the prediction & fit the model
y_kmeans = kmeansmodel.fit_predict(X)


# In[41]:


# Visualización de los clusters
# 
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=80, c='red', label='Customer 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=80, c='blue', label='Customer 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=80, c='yellow', label='Customer 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=80, c='cyan', label='Customer 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=80, c='black', label='Customer 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='magenta', label='Centroids')
plt.title("Cluster of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()


# ### Resume :
# 
# **In the graph we can see**: 
# 
# 1.**high salaries**, lower spending. 
# 
# On the other hand, 
# 
# 2.**low average salaries**, they spend more.
# 
# 3.**By managing this information**, we know our customers better and can promote our products more effectively.
