#!/usr/bin/env python
# coding: utf-8

# ### Support Vector Machine

# ### Loading the data

# In[1]:


#import the libraries 
import pandas as pd
import numpy as np 


# In[2]:


#import load wine
from sklearn.datasets import load_wine


# In[3]:


#store it into a variable 
wine = load_wine()


# In[4]:


#a Dcitionary key
wine.keys()


# In[7]:


#look at the DESCR column
print(wine.DESCR)
#13 numeric attributes
#3 classes


# In[11]:


wine.keys()


# In[12]:


# look at the column name = feature_names
wine["feature_names"]


# In[13]:


#an array
wine.data


# ##### ...start with creating a pandas data frame 
# 

# In[14]:


df = pd.DataFrame(wine.data, columns=wine.feature_names)
df.head()
# but we dont have the target


# In[20]:


# create one more data frame as df_target
df_target = pd.DataFrame(wine.target,columns=['WineType'])
df_target['WineType'].unique()


# In[21]:


df_target.head()


# ### Scaling 

# In[22]:


#df_describe = frist df
df.describe()
#look at the mean = the date are not scale, on the same scale


# In[23]:


#call the StandardScaler
from sklearn.preprocessing import StandardScaler


# In[24]:


#create an object and the instance 
ss = StandardScaler()


# In[26]:


#fit_transform
arr = ss.fit_transform(df)
#data transformed into a NP Array


# In[27]:


#### ...re create the first DF 
dfs = pd.DataFrame(arr, columns=wine.feature_names)


# In[28]:


dfs.head()


# ### Training and Predicting 

# In[29]:


#its time to split the data 
from sklearn.model_selection import train_test_split


# In[30]:


#X values 
X = dfs


# In[36]:


#y = target
y = df_target['WineType']


# ##### train_test_split(shift+tab) and paste = X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# In[37]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[34]:


#lets import support_vector_classifier
from sklearn.svm import SVC


# In[38]:


#create the instance 
svc = SVC()


# In[39]:


#So, lets fit the model
svc.fit(X_train, y_train)


# #### ...make some predictions

# In[40]:


#prediction 1 
y_pred = svc.predict(X_test)


# In[41]:


#meassures the effectivenes or the accuracy of the result
from sklearn.metrics import classification_report, confusion_matrix


# In[42]:


#confusion matrix 
print(confusion_matrix(y_test, y_pred))
#notice the diagonal the values look good


# In[44]:


#classification_report 
print(classification_report(y_test, y_pred))
#98% accuracy is extremely good


# #### lets see without scaling what happens

# In[45]:


X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=42)  #df


# In[46]:


#So, lets fit the model
svc.fit(X_train, y_train)
#prediction 2 
y_pred2 = svc.predict(X_test)


# In[47]:


#confusion matrix 
print(confusion_matrix(y_test, y_pred2))
#classification_report 
print(classification_report(y_test, y_pred2))
#notice 71% accuracy


# In[ ]:




