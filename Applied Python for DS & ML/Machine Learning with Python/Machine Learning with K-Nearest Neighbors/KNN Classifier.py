#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">K-Nearest Neighbors Classifier - The Random Data Set</font></b></h1></center>

# In[73]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.datasets import make_blobs
from mlxtend.plotting import plot_decision_regions
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV


# #### Generating the database

# In[19]:


#define variables
#inputs contain arrays of the x-andy-coordinates
#target is a one dimensional array and holds the labels of each data point
inputs, target = make_blobs(n_samples = 1000, 
                            centers = [(-3, 3), (0, 0), (2,2)],
                            random_state = 365) #1000 numbers of datapoints


# In[20]:


inputs.shape, target.shape
#1000 datapoints
#2 are features, represente x,y


# #### Lets put the 2 created variables into pandas DataFrame 

# In[21]:


data = pd.DataFrame(data = inputs, columns = ['Feature 1', 'Feature 2'])
data['Target'] = target


# In[22]:


data


# #### Plotting the database 

# In[23]:


knn_palette = sns.color_palette(['#000C1F', '#29757A', '#FF5050'])
knn_palette


# In[24]:


sns.set()

plt.figure(figsize = (16, 9))

sns.scatterplot(x = 'Feature 1', y = 'Feature 2',
               data = data,
               hue = 'Target', palette = knn_palette, 
                markers = [',', '^', 'P'],
               style = 'Target',
               s = 100)


# #### Visualizing the distribution of the points

# In[25]:


sns.set()

sns.jointplot(x = 'Feature 1', y = 'Feature 2',
             data  = data,
             hue = 'Target',
             palette = knn_palette,
             height = 10,
             s = 100,
             legend = True);


# #### Creating a train-test-split

# In[31]:


x_train, x_test, y_train, y_test = train_test_split(inputs, target,
                                                   test_size = 0.2,
                                                   random_state = 365, 
                                                   stratify = target)


# #### Creating the model

# In[57]:


clf = KNeighborsClassifier(n_neighbors = 30, weights = 'uniform')

clf.fit(x_train, y_train)


# #### Predicting a sample

# In[33]:


feature_1 = -0.18
feature_2 = 3.2


# In[47]:


clf.predict([[feature_1, feature_2]])


# In[49]:


#index
neighbors = clf.kneighbors([[feature_1, feature_2]])
neighbors


# #### Visualizing the neighbors

# In[39]:


sns.set()

plt.figure(figsize = (16, 9))

sns.scatterplot(x = x_train[:, 0], y = x_train[:, 1],
                hue = y_train,
                palette = knn_palette,
                markers = [',', '^', 'P'],
                style = y_train,
                s = 100,
                legend = True);

sns.scatterplot(x = [feature_1], y = [feature_2],
               style = [feature_2],
               markers = ['o'],
               s = 100,
               legend = False);


# In[44]:


sns.set()

plt.figure(figsize = (16, 9))

sns.scatterplot(x = x_train[:, 0], y = x_train[:, 1],
                hue = y_train,
                palette = knn_palette,
                markers = [',', '^', 'P'],
                style = y_train,
                s = 100,
                legend = True);

sns.scatterplot(x = [feature_1], y = [feature_2],
               style = [feature_2],
               markers = ['o'],
               s = 100,
               legend = False);

plot_x_train = []
plot_y_train = []

for i in neighbors[1]:
    plot_x_train.append(x_train[i, 0])
    plot_y_train.append(x_train[i, 1])
    
plt.scatter(plot_x_train,
            plot_y_train,
            s = 200, facecolors='none', edgecolors='r')


# #### Getting the parameters of the model

# In[45]:


clf.get_params()


# #### Drawing the decision regions

# In[51]:


x_train.shape #800 samples / 2 features


# In[58]:


start = time.time()

plt.figure(figsize=(16, 9))

plot_decision_regions(X=x_train, y=y_train,
                      clf=clf,
                      markers=[',', '^', 'P'],
                      colors='#000c1f,#29757a,#ff5050',
                      scatter_kwargs={'s': 100, 'edgecolor': 'white', 'alpha': 1},
                      legend=0)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

end = time.time()

print(f'Time elapsed: {round(end - start, 1)} seconds')


# #### Getting the error rates of a set of models

# In[60]:


error_uniform = []
error_distance = []

k_range = range(1, 51) # 1 to 50 numbers

for k in k_range:
    clf = KNeighborsClassifier(n_neighbors = k, weights = 'uniform')
    clf.fit(x_train, y_train)
    predictions = clf.predict(x_test)
    error_uniform.append(1 - accuracy_score(y_test, predictions))
    
    clf = KNeighborsClassifier(n_neighbors = k, weights = 'distance')
    clf.fit(x_train, y_train)
    predictions = clf.predict(x_test)
    error_distance.append(1 - accuracy_score(y_test, predictions))


# #### Plotting the error rates as a function of the number of neighbors

# In[62]:


plt.figure(figsize = (16, 9))

plt.plot(k_range, error_uniform, c = 'blue', linestyle = 'solid',
         marker = 'o', markerfacecolor = 'red', label = 'Error uniform')

plt.plot(k_range, error_uniform, c = 'green', linestyle = 'dashed',
         marker = 'o', markerfacecolor = 'red', label = 'Error distance')
         
plt.legend()
         
plt.xlabel('K-value')
plt.ylabel('Error rate');


# #### Choosing a set of parameters to test

# In[64]:


#GridSearchCV test all posibles parameters using Cross Validation
parameters = {'n_neighbors': range(1, 51),
              'weights': ['uniform', 'distance']}


# #### Create an instance of the GridSearchCV class

# In[65]:


grid_search = GridSearchCV(estimator = KNeighborsClassifier(),
                           param_grid = parameters,
                           scoring = 'accuracy')


# In[66]:


# create each model combination parameters and fit the model to the training data
grid_search.fit(x_train, y_train)


# In[67]:


# best performance parameters
# 10 
grid_search.best_params_


# In[69]:


# best estimator
clf = grid_search.best_estimator_


# In[70]:


clf


# In[71]:


#accuracy
grid_search.best_score_


# #### Make predictions on the test dataset

# In[72]:


y_test_pred = clf.predict(x_test)
y_test_pred.shape


# #### Construc the confusion matrix 

# In[74]:


sns.reset_orig()

ConfusionMatrixDisplay.from_predictions(
    y_test, y_test_pred,
    labels = clf.classes_,
    cmap = 'magma'
);


# ####  Print out the classification report

# In[77]:


print(classification_report(y_test, y_test_pred))

