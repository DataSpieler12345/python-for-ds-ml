#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Regression Analysis</font></b></h1></center>

# ## Imports

# In[2]:


import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# ## Read the data

# In[5]:


df = pd.read_csv(r"./data/winequality-red.csv")
df.head()


# ## Separate data (x) and label (y)

# In[6]:


x = df.loc[:, : "alcohol"]
y = df["quality"]


# ## Scale the data

# In[8]:


scaler = StandardScaler()
x = scaler.fit_transform(x)
x


# ## Split in train and test set 

# In[9]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


# ## Least Absolut Shrinkage & Selection Operator 

# In[10]:


lasso = Lasso(alpha=0.001)
lasso.fit(x_train, y_train)


# ## Support Vector Regression

# In[12]:


svr = SVR(C=8, epsilon=0.2, gamma=0.5)
svr.fit(x_train, y_train)


# ## Predict LASSO

# In[13]:


y_pred_lasso = np.round(np.clip(lasso.predict(x_test), 1, 10)).astype(int)
np.round(1 - mean_squared_error(y_test, y_pred_lasso) / y_test.std(), 2)


# ## Predict SVR

# In[14]:


y_pred_svr = np.round(np.clip(svr.predict(x_test), 1, 10)).astype(int)
np.round(1 - mean_squared_error(y_test, y_pred_svr) / y_test.std(), 2)

