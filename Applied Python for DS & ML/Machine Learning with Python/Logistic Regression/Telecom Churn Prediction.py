#!/usr/bin/env python
# coding: utf-8

# ### Telecom Churn Prediction

# Project List :
# Problem Statement: This is a telecom dataset. The columns are self-explanatory.
# https://archive.ics.uci.edu/ml/datasets/Iranian+Churn+Dataset
# 
# * Data Set Information:
# 
# This dataset is randomly collected from an Iranian telecom company s database over a period of 12 months.
# 
# A total of 3150 rows of data, each representing a customer, bear information for 13 columns. 
# 
# The attributes that are in this dataset are call failures, frequency of SMS, number of complaints, number of distinct calls, subscription length, age group, the charge amount, type of service, seconds of use, status, frequency of use, and Customer Value.
# 
# All of the attributes except for attribute churn is the aggregated data of the first 9 months. The churn labels are the state of the customers at the end of 12 months. The three months is the designated planning gap.
# 
# * Attribute Information:
# 
# Anonymous Customer ID
# 
# Call Failures: number of call failures
# 
# Complains: binary (0: No complaint, 1: complaint)
# 
# Subscription Length: total months of subscription
# 
# Charge Amount: Ordinal attribute (0: lowest amount, 9: highest amount)
# 
# Seconds of Use: total seconds of calls
# 
# Frequency of use: total number of calls
# 
# Frequency of SMS: total number of text messages
# 
# Distinct Called Numbers: total number of distinct phone calls
# 
# Age Group: ordinal attribute (1: younger age, 5: older age)
# 
# Tariff Plan: binary (1: Pay as you go, 2: contractual)
# 
# Status: binary (1: active, 2: non-active)
# 
# Churn: binary (1: churn, 0: non-churn) - Class label
# 
# Customer Value: The calculated value of customer
# 
# * Objective:
# 
# The objective of the project is to create a model to predict if a customer will churn or not.
# 
# Explain whether it is a case of supervised or unsupervised learning.
# 
# Later, explain the choice of the performance evaluation metric.

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
df_data = pd.read_csv("data/Customer Churn.csv")


# In[3]:


#Outcome columns is the target column 
# null datapresent in this dataset
df_data.info()


# In[5]:


df_data.describe()


# In[6]:


df_data.head()


# In[7]:


df_data.isnull().sum()


# In[9]:


df_data.columns


# In[12]:


df_data.dtypes


# In[13]:


df_data.Churn.value_counts()


# In[14]:


df_data.Age.value_counts()


# In[15]:


# Plot the outcome variable 
sns.countplot(x= 'Churn', data=df_data)
plt.show()


# In[17]:


# Correlation Plot 
sns.heatmap(df_data[df_data.columns[:14]].corr(),annot=True,cmap='RdYlGn')
fig=plt.gcf()
fig.set_size_inches(10,8)
plt.show()


# ### The objective of the project is to create a model to predict if a customer will churn or not.

# In[19]:


#Split the dataset in features and target variable 
feature_cols = ['Call  Failure','Complains','Subscription  Length','Charge  Amount','Seconds of Use','Frequency of use','Frequency of SMS','Distinct Called Numbers','Age Group','Tariff Plan','Status','Age','Customer Value']
X = df_data[feature_cols] #features
y = df_data.Churn #Target variable


# In[20]:


#Split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)


# In[21]:


X_train.shape


# In[22]:


#Import the class
from sklearn.linear_model import LogisticRegression

#Instantiate the model
logreg = LogisticRegression(max_iter=10000)

#fit the model with data
logreg.fit(X_train,y_train)

#Predict for test dataset
y_pred=logreg.predict(X_test)


# In[23]:


#Import the metrics class
from sklearn import metrics 


# In[24]:


#Create Confusion Matrix 
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix


# In[25]:


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


# In[26]:


# Print the model evaluation metrics 

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))


# In[27]:


#testing the models
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# In[30]:


# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


# In[31]:


# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)


# ### Explain whether it is a case of supervised or unsupervised learning.

# This is a case of supervised learning because the objective is to create a model to predict whether a customer will churn or not, which is a binary classification problem. The dataset provides labeled data with the "Churn" column indicating whether a customer has churned or not.

# ### Later, explain the choice of the performance evaluation metric.

# The choice of performance evaluation metrics depends on the specific requirements and priorities of the project. Let's discuss the values of the evaluation metrics for the given model:
# 
# * Accuracy: 0.8858
# Accuracy measures the overall correctness of the predictions, indicating the proportion of correctly predicted churn or non-churn cases out of the total predictions. In this case, the model achieves an accuracy of 0.8858, which means that approximately 88.58% of the predictions are correct.
# 
# * Precision: 0.8205
# Precision is the proportion of correctly predicted positive cases (churn) out of all predicted positive cases. A higher precision indicates a lower rate of false positives, meaning that the model is good at correctly identifying actual churn cases. Here, the precision is 0.8205, suggesting that about 82.05% of the predicted churn cases are true positives.
# 
# * Recall: 0.4571
# Recall, also known as sensitivity or true positive rate, measures the proportion of correctly predicted positive cases (churn) out of all actual positive cases. A higher recall indicates a lower rate of false negatives, meaning that the model is good at capturing actual churn cases. In this case, the recall is 0.4571, indicating that approximately 45.71% of the actual churn cases are correctly predicted by the model.
# 
# * F1 Score: 0.5872
# The F1 score is the harmonic mean of precision and recall, providing a balanced measure of the model's performance. It considers both false positives and false negatives. A higher F1 score indicates a better balance between precision and recall. The F1 score for this model is 0.5872, which suggests a reasonable balance between correctly identifying churn cases and minimizing false positives and false negatives.
# 
# Based on these evaluation metrics, we can interpret the model's performance as follows: The model achieves a high accuracy, indicating that a large proportion of the predictions are correct. The precision score indicates that the model is good at correctly identifying churn cases, with a relatively low rate of false positives. However, the recall score is relatively low, indicating that the model may miss a significant number of actual churn cases, resulting in a higher rate of false negatives. The F1 score, being the harmonic mean of precision and recall, provides a balanced measure, taking into account both false positives and false negatives.
# 

# In[ ]:




