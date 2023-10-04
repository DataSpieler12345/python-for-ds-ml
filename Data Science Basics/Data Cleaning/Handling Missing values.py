#!/usr/bin/env python
# coding: utf-8

# ## Handling Missing Values

# In[12]:


from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd


# In[4]:


#create data
#the default value for a missing feature entry is NaN
data = np.array([[1,np.nan,2],[2,3,np.nan],[-1,4,2]])

data


# In[9]:


# Create an instance of SimpleImputer
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data using the imputer
data_imputed = imputer.fit_transform(data)

print(data_imputed)


# In[10]:


# Create an instance of SimpleImputer
imputer = SimpleImputer(strategy='median')

# Fit and transform the data using the imputer
data_imputed = imputer.fit_transform(data)


print(data_imputed)


# In[11]:


# Create an instance of SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')

# Fit and transform the data using the imputer
data_imputed = imputer.fit_transform(data)


print(data_imputed)


# ### Dictionary of Lists

# In[13]:


dict = {'First Score':[100,90,np.nan,95],
       'Second Score':[30,45,56,np.nan],
       'Third Score':[np.nan,40,80,98]}

#creating a dataframe from list 
df = pd.DataFrame(dict)

#using isnull() function
df.isnull()


# In[14]:


#filling missing values using fillna()
df.fillna(0)


# In[15]:


#filling null values using fillna() function 
#code 3: Filling null value with the next ones
df.fillna(method='bfill')


# In[ ]:




