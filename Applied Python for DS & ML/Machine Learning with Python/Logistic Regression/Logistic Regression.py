#!/usr/bin/env python
# coding: utf-8

# ### Logistic Regression Implementation

# In[1]:


# Import the Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")


# In[2]:


# Load the dataset
df_pima = pd.read_csv("data/diabetes.csv")


# In[3]:


#Outcome columns is the target column 
# null datapresent in this dataset
df_pima.info()


# In[4]:


df_pima.describe()


# In[5]:


df_pima.head()


# In[8]:


df_pima.isnull().sum()


# In[10]:


# Plot the outcome variable 
sns.countplot(x= 'Outcome', data=df_pima)
plt.show()


# In[15]:


# Correlation Plot 
sns.heatmap(df_pima[df_pima.columns[:8]].corr(),annot=True,cmap='RdYlGn')
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.show()


# In[17]:


#Split the dataset in features and target variable 
feature_cols = ['Pregnancies','Insulin','BMI','Age','Glucose','BloodPressure','DiabetesPedigreeFunction']
X = df_pima[feature_cols] #features
y = df_pima.Outcome #Target variable


# In[18]:


#Split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)


# In[19]:


X_train.shape


# In[20]:


#Import the class
from sklearn.linear_model import LogisticRegression

#Instantiate the model
logreg = LogisticRegression(max_iter=10000)

#fit the model with data
logreg.fit(X_train,y_train)

#Predict for test dataset
y_pred=logreg.predict(X_test)


# In[21]:


#Import the metrics class
from sklearn import metrics 


# In[22]:


#Create Confusion Matrix 
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix


# In[27]:


class_names = [0, 1]  # Nombres de las clases
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

# Crear un mapa de calor (heatmap)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g', ax=ax)
plt.tight_layout()
plt.title('Confusion Matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

plt.show()


# In[28]:


# Print the model evaluation metrics 

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))


# In[ ]:




