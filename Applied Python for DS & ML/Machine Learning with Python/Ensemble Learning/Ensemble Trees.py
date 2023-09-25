#!/usr/bin/env python
# coding: utf-8

# ### Ensemble Trees

# In[45]:


import pandas as pd
import numpy as np

from sklearn.model_selection import GridSearchCV #hyperparameter turning
from sklearn.model_selection import train_test_split #easily split our dataset
from sklearn.model_selection import cross_val_score #create a cross-validation score
from sklearn.model_selection import RandomizedSearchCV #perfom a randomized grid search

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier

import warnings
warnings.filterwarnings("ignore")


# #### load the data

# In[3]:


df = pd.read_csv('data/Elections_Data.csv')
df.shape


# In[4]:


df


# #### Extracting the predictors from the dataframe 

# In[5]:


cols = ['heat_jul','heat_aug','heat_sep','heat_oct','unemployment','inflation']
X = df[cols]
X.shape


# In[6]:


X


# #### Extracting the response variable from the dataframe 

# In[7]:


y = df['incumbent_won']


# #### Reshaping the data to use in Classifier

# In[9]:


y_reshaped = y.to_numpy().reshape((21, 1))


# In[10]:


print(y_reshaped.shape)


# #### Training and Testing Splits

# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(X_train.shape)
print(y_train.shape)


# ### Gradient Boosting Machine
# 
# #### Hyperparameter tuning: https://medium.com/all-things-ai/in-deph-parameter-tuning-for-gradient-boosting

# In[15]:


#Random Grid Search with Gradient Boosting
#How fast the algorithm learns
learning_rate = [0.001, 0.01, .05]
#Number of trees in the forest
n_estimators = [200, 1000, 2000]
#Maximum number of levels in tree
max_depth = np.linspace(1, 21, num=21, dtype=int, endpoint=True)
#Minimum number of samples required to split a node
min_samples_split = np.linspace(0.1, 1.0, num=10, endpoint=True)
#Minumum number of samples required at each leaf node
min_samples_leaf = np.linspace(0.1, 0.5, num=5, endpoint=True)
#Method of selecting samples for training each tree
max_features = list(range(1, X_train.shape[1]))

#Create the random grid
random_grid = {'learning_rate': learning_rate,
               'n_estimators': n_estimators,
               'max_depth': max_depth,             
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'max_features': max_features}


# In[16]:


# Use the random grid to search for best hyperparameters
# First, create the base model to tune
gbm = GradientBoostingClassifier()
# Random search of parameters, using 3-fold cross validation
# Search across 100 different combinations and use all available cores
gbm_random = RandomizedSearchCV(estimator=gbm, param_distributions=random_grid, n_iter=100, cv=5, verbose=2, random_state=42)
# Fit the random search model
gbm_random.fit(X_train, y_train)

# Best parameters
print(gbm_random.best_params_)


# #### After Random Search do Grid Search based on the results

# Result = {'n_estimators': 200, 'min_samples_split': 0.2, 'min_samples_leaf': 0.2, 'max_features': 2, 'max_depth': 4, 'learning_rate': 0.001}

# In[18]:


#### Create the parameter grid based on the results of random search
param_grid = {
	'n_estimators': [200, 300],
    'min_samples_split': [0.2, 0.3], 
    'min_samples_leaf': [0.2, 0.3],
    'max_features': [1, 2],
    'max_depth': [2, 4], 
    'learning_rate': [0.001, 0.005]}

#### Instantiate the grid search model
grid_search = GridSearchCV(estimator=gbm, param_grid = param_grid, cv=5, verbose=2)

#### Training with the Grid Search 
grid_search.fit(X_train, y_train)

#### Print the best parameters found by the grid search
print(grid_search.best_params_)


# #### Predictions for the GBM

# In[20]:


gbm = GradientBoostingClassifier(learning_rate = .001, max_depth = 2, max_features = 1, min_samples_leaf = 0.3, min_samples_split = 0.3, n_estimators = 300)
gbm.fit(X_train, y_train)
scores = cross_val_score(gbm, X_train, y_train, cv = 5)
np.mean(scores)
print('the average validation accuracy across our 5 folds is ' + str(np.mean(scores)))


# ### Grid Search with Random Forest

# In[36]:


#### Number of trees in random forest
n_estimators = [400, 1000]
#### Number of features to consider at every split
max_features = ['sqrt']
#### Maximum number of Levels in tree
max_depth = [1, 7, 12]
#### Minimum number of samples required to split a node 
min_samples_split = [2, 5]
#### Minimin number of samples required at each leaf node 
min_samples_leaf = [1, 3]
#### Method of selecting samples for training each tree 
bootstrap = [True]

#### Create the random grid 
#Create the random grid
random_grids = {'n_estimators': n_estimators,
               'max_depth': max_depth,             
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'max_features': max_features,
               'bootstrap': bootstrap}


# #### Create a base model 

# In[37]:


rf = RandomForestClassifier()

#### Instantiate the grid search model 
grid_search = GridSearchCV(estimator = rf, param_grid = random_grids, cv = 5, verbose = 2)

#### Training with the Grid Search
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)


# #### Predictions for the Random Forest
# 
# {'bootstrap': True, 'max_depth': 1, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 400}

# In[38]:


rf = RandomForestClassifier(bootstrap = True, max_depth = 1, max_features = 'sqrt', min_samples_leaf = 1, min_samples_split = 2, n_estimators = 400)
rf.fit(X_train, y_train)
scores = cross_val_score(rf, X_train, y_train, cv = 5)
np.mean(scores)
print('the average validation accuracy across our 5 folds for Random Forest is ' + str(np.mean(scores)))


# #### Creating a Bagging Classifier with hot hyperparameter tuning 

# In[39]:


bag  = BaggingClassifier(n_estimators = 600, max_samples = 0.5, max_features = 0.5, random_state = 42)
bag.fit(X_train, y_train)
scores = cross_val_score(bag, X_train, y_train, cv = 5)
np.mean(scores)
print('the average validation accuracy across our 5 folds for Bagging is ' + str(np.mean(scores)))


# #### Creating predictions for the gbm

# In[40]:


y_pred = gbm.predict(X_test)
rf.score(X_test, y_test)


# #### Viewing the predictions

# In[41]:


predictions = gbm.predict(X)
predictions


# #### Adding the predictions to the dataframe

# In[42]:


df['predictions'] = predictions
cols_to_keep = ['Year','incumbent_won','predictions']
df[cols_to_keep]


# #### Hand coding the accuracy of the model predictions 

# In[46]:


df['correct'] = 0
for i in range(len(df)):
    if df['incumbent_won'][i] == df['predictions'][i]:
        df['correct'][i] = 1
accuracy = 1 - ((len(df) - np.sum(df['correct']))/len(df))
print('With this simple model we could say we have correctly predicted ' + str(accuracy) +'00' + ' percent of USE presidential elections since the year 1936')

