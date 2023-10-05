#!/usr/bin/env python
# coding: utf-8

# ## Outlier Analysis 

# In[1]:


from sklearn.datasets import load_boston
boston = load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names


# In[5]:


import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
column_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None, names=column_names)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

print("Column Names:")
print(column_names)
print("\nData:")
print(raw_df)


# In[7]:


raw_df.head()


# ### Discover outlier with vistualization tools 

# #### Using Boxplot

# In[8]:


import seaborn as sns 
sns.boxplot(x=raw_df['DIS'])
#point between 10 to 12, these are outliers


# #### Using Scatter plot

# In[9]:


#import matplotlib module for ploting scatterplot
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(raw_df['INDUS'], raw_df['TAX'])
ax.set_xlabel('Proportion of non-retail business acres per town')
ax.set_ylabel('Full-value property-tax rate per $10,000')
plt.show()

#points which are far from the population  are outliers


# #### Discover outliers with mathematical function

# ##### Using Z-score

# In[11]:


from scipy import stats
import numpy as np
z = np.abs(stats.zscore(raw_df))
print(z)


# In[12]:


#define a threshold to identify an outlier
threshold = 3
print(np.where(z > 3))


# In[ ]:


#The first array contains the list of row numbers and second array 
#respective column numbers, which mean z[78][1] have a Z-score higher than 3


# ##### Using IQR score

# In[24]:


#find quantile
Q1 = raw_df.quantile(0.25)
Q3 = raw_df.quantile(0.75)
#formula for interquartile range 
IQR = Q3 - Q1
print(IQR)


# ##### Working with Outliers: Correcting, Removing

# In[ ]:


raw_df_o = raw_df[(z < 3).all(axis=1)]


# In[27]:


#result with outlier
raw_df.shape

