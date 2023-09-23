#!/usr/bin/env python
# coding: utf-8

# ### Python Implementation of Decision Tree 

# In[20]:


#import the required libraries 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import sklearn 

from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.metrics import accuracy_score,recall_score,precision_score,confusion_matrix,f1_score
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")


# In[2]:


#print sklearn version 
print(sklearn.__version__)


# #### Import the file using Pandas 

# In[3]:


url = "https://github.com/mawalz05/PLSC481M_Forecasting_Elections/raw/master/Elections_Data.csv"
df = pd.read_csv(url)
df


# #### Extracting the predictors from the dataframe 

# In[4]:


cols = ['heat_jul','heat_aug','heat_sep','heat_oct','unemployment','inflation']
X = df[cols]
X.shape


# In[5]:


X


# #### Extracting the response variable from the dataframe 

# In[6]:


y = df['incumbent_won']
y


# #### Reshaping the data to use in Classifier

# In[12]:


y = np.array(y)
y = y.reshape(21, 1)

print(y.shape)


# #### Decision Tree Classifier without pruning

# In[13]:


clf = DecisionTreeClassifier(random_state = 42)
clf.fit(X, y)
clf.score(X, y)


# #### Decision Tree Classifier with pruning 

# In[14]:


clf = DecisionTreeClassifier(max_depth = 2, min_samples_leaf = 2, random_state = 42)
clf.fit(X, y)
clf.score(X, y)


# #### Training and Testing Splits

# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=333)
print(X_train.shape)
print(y_train.shape)


# #### Decision Tree Classification on the training set

# In[17]:


clf = DecisionTreeClassifier(random_state = 42)
clf.fit(X_train, y_train)
clf.score(X_train, y_train)


# #### Decision Tree Predictions on the testing set | confusion_matrix | accuracy of classification task

# In[18]:


clf.predict(X_test)
clf.score(X_test, y_test)
#overfitting


# In[21]:


clf = DecisionTreeClassifier(random_state = 42).fit(X_train,y_train)
print("Training:"+str(clf.score(X_train,y_train)))
print("Test:"+str(clf.score(X_test,y_test)))
pred = clf.predict(X_test)
confusion_matrix = confusion_matrix(y_true=y_test,y_pred=pred)

sns.heatmap(confusion_matrix,annot=True,annot_kws={"size":16})
plt.show()

confusion_matrix


# #### Plotting the Decision Tree | generating the Tree

# In[22]:


from sklearn import tree
tree.plot_tree(clf)


# In[23]:


X_train
#variable heat_oct is our more importan predicter
#x[3] 


# #### Another way to interpret the Decision Tree

# In[25]:


text_presentation = tree.export_text(clf)
print(text_presentation)
#variable heat_oct is our more important predicter
#feature_3


# #### Which variables are of importance?

# In[27]:


for name, importance in zip(X_train.columns, clf.feature_importances_):
    print(name, importance)

