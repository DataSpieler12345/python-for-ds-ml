#!/usr/bin/env python
# coding: utf-8

# ## Decision Trees Classifier

# ### Loading the Data 

# In[1]:


import pandas as pd
import numpy as np 


# #### Dataset link: https://archive.ics.uci.edu/dataset/19/car+evaluation

# #. Attribute Values:
# 
#    buying: v-high, high, med, low
#    maint: v-high, high, med, low
#    doors: 2, 3, 4, 5-more
#    persons: 2, 4, more
#    lug_boot: small, med, big
#    safety: low, med, high

# In[2]:


df = pd.read_csv('./Data/car.data')
df.head()
#notice that there is no column information


# In[3]:


#lets create the headers manually as a list + class
headers = [
'buying',
'maint',
'doors',
'persons',
'lug_boot',
'safety',
'class']


# In[4]:


#chet the created list to verify if everything is correct 
headers


# In[5]:


# put the new created headers with the table of data 
df.columns = headers
df.head()


# ### Preliminary Analysis of Data 

# In[6]:


#shape of the dataset 
df.shape
#rows = 1727 
#columns = 7


# In[7]:


#info
df.info()
#all of them are object / string and we need numeric data


# In[8]:


#describe
df.describe()
#count = for all 1727
#unique = there are only 3 or 4 values
#calls columns is that we want to predict 


# In[10]:


#lets see if there null values
df.isnull().any()


# In[11]:


df.isnull().sum()


# In[12]:


#look at the class column and unique values 
df['class'].unique()


# In[14]:


#even better, call the value_counts
df['class'].value_counts()


# ### Preprocessing

# In[15]:


#the data frame 
df.head()
#how to convert the data into numeric data?


# In[17]:


#doors column
df['doors'].value_counts()
#notice the 5more, as string


# In[18]:


df['doors']
#datatype = object


# In[19]:


#call again the df
df.head()


# #### ...preprocessing

# In[21]:


#OrdinalEncoder 
from sklearn.preprocessing import OrdinalEncoder


# In[22]:


#create the instance
enc = OrdinalEncoder()


# In[25]:


#create the fit_transform method and transform all the column without class column 
ar = enc.fit_transform(df.drop('class', axis=1))
#result = a numpy array


# In[26]:


#lets tranform the numpy array into a pandas DF
dft = pd.DataFrame(ar, columns=headers[:-1]) #exlude class column
dft.head()


# In[27]:


df.head()
# 7 columns
# contain string values 


# In[28]:


#dft.info()
dft.info()
# all are numeric values
# 6 columns


# ### Decision Tree Classifier

# In[29]:


dft.head()


# In[30]:


# X as attribute 
X = dft


# In[31]:


# y as target (df because in dft we dont have class column)
y = df['class']


# #### ...split them now 

# In[32]:


#train_test_split
from sklearn.model_selection import train_test_split


# ##### train_test_split() / shift + tab to find the line that we will use...
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# In[33]:


#create the training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[34]:


#import the algorithm = Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier


# In[35]:


#after that, Create an object and the instance 
tree = DecisionTreeClassifier()
#gini is by default but its work also with entropy, same.


# #### ...train the model

# In[36]:


#train the model
tree.fit(X_train, y_train)
#the model is ready to make predictions


# In[37]:


#make predictions
y_pred = tree.predict(X_test)


# In[38]:


#check how good the model is...classification_report, confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix


# In[40]:


print(classification_report(y_test, y_pred))
# the result show = really good classifier


# In[41]:


#confusion matrix
print(confusion_matrix(y_test, y_pred))
#we have four classes, it will only 2 by 2 matrix 
# accuracy very high = 120,15,399,24= values)


# ## Random Forest Classifier

# In[42]:


#call the random Forest Classifier
from sklearn.ensemble import RandomForestClassifier


# In[43]:


#lets create the random forest classifier object and the instance 
rfc = RandomForestClassifier()


# In[44]:


#train the model /object
rfc.fit(X_train, y_train)


# In[45]:


#lets make some predictions
y_pred_rfc = rfc.predict(X_test)


# In[46]:


#call again the classification_report and confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix


# In[47]:


#check the classification_report for random forest
print(classification_report(y_test, y_pred_rfc)) #y_pred_rfc
#this is the classification report 
#notice the weighted avg 0.96


# In[48]:


# print the classification report for the decision tree
print(classification_report(y_test, y_pred)) #y_pred
#notice the weighted avg 0.98
#quit better 


# In[49]:


#confusion_matrix for Random forest
print(confusion_matrix(y_test, y_pred_rfc))


# In[50]:


#confusion matrix for the Decision Tree 
print(confusion_matrix(y_test, y_pred))


# In[ ]:




