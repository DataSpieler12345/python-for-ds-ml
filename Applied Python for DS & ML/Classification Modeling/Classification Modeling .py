#!/usr/bin/env python
# coding: utf-8

# ### Classification Modeling - Penguins Dataset

# #### Preparation Part 1: Loading & Exploring Penguins Data 

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import statsmodels.api as sm

#classifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
#accuracy of the classifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

import warnings
warnings.filterwarnings("ignore")


# #### Load the Penguins dataset

# In[2]:


df_penguins = sns.load_dataset("penguins")


# In[3]:


df_penguins.info()


# In[4]:


df_penguins.head(5)


# In[5]:


df_penguins.describe()


# In[6]:


df_penguins.describe(include = ["O"])


# In[7]:


df_penguins = df_penguins[df_penguins["sex"].notnull()]


# In[8]:


df_penguins.describe(include = ["O"])


# In[9]:


df_penguins.isnull().sum()


# In[10]:


df_penguins.columns


# In[11]:


sns.set(color_codes=True)
colors = sns.color_palette("bright")

fig, axes = plt.subplots(2,2, figsize = (10,10))

sns.distplot(df_penguins["bill_length_mm"], color = colors[0], ax = axes[0,0])
sns.distplot(df_penguins["bill_depth_mm"], color = colors[1], ax = axes[0,1])
sns.distplot(df_penguins["flipper_length_mm"], color = colors[2], ax = axes[1,0])
sns.distplot(df_penguins["body_mass_g"], color = colors[3], ax = axes[1,1])

plt.suptitle("Distribution of Quantitativ Variables", y=1.01, size=16)
plt.tight_layout()
plt.show()


# In[12]:


sns.set(color_codes=True)
colors = sns.color_palette("bright")

fig, axes = plt.subplots(2,2, figsize = (10,10))

sns.boxplot(y=df_penguins["bill_length_mm"], color = colors[0], ax = axes[0,0])
sns.boxplot(y=df_penguins["bill_depth_mm"], color = colors[1], ax = axes[0,1])
sns.boxplot(y=df_penguins["flipper_length_mm"], color = colors[2], ax = axes[1,0])
sns.boxplot(y=df_penguins["body_mass_g"], color = colors[3], ax = axes[1,1])

plt.suptitle("Distribution of Quantitativ Variables", y=1.01, size=16)
plt.tight_layout()
plt.show()


# #### Preparation Part 2: Cleaning & Preparing Penguins Data

# In[13]:


df_penguins.columns


# In[14]:


sns.set(color_codes=True)
colors = sns.color_palette("bright")

fig, axes = plt.subplots(1,3, figsize = (10,6))

sns.countplot(x="species", data = df_penguins, ax = axes[0])
sns.countplot(x="island", data = df_penguins, ax = axes[1])
sns.countplot(x="sex", data = df_penguins, ax = axes[2])

#quick for loop to rotate the axis labels
for ax in fig.axes:
    ax.tick_params(labelrotation=90)
    
plt.suptitle("Categorical Variable Frequency", y=1.01, size=16)
plt.tight_layout()
plt.show()


# In[15]:


df_penguins = df_penguins.drop(columns = "island", axis=0) 


# In[16]:


df_penguins.head()


# In[17]:


df_penguins["species"].value_counts()


# In[18]:


adelie = df_penguins[df_penguins["species"]=="Adelie"].sample(n=50)
gentoo = df_penguins[df_penguins["species"]=="Gentoo"].sample(n=50)
chinstrap = df_penguins[df_penguins["species"]=="Chinstrap"].sample(n=50)


# In[19]:


type(chinstrap)


# In[20]:


new_peng = pd.concat([adelie, gentoo, chinstrap], axis = 0)


# In[21]:


#50 for each example
new_peng


# In[22]:


#spliot categorical variables
peng_sex = pd.get_dummies(new_peng["sex"])


# In[23]:


#drop sex from new_peng DF
new_peng = new_peng.drop(columns = "sex", axis = 0)


# In[24]:


peng_sex


# In[25]:


new_peng


# In[28]:


#concatenate peng_sex & new_peng DF 
final_df = pd.concat([new_peng, peng_sex], axis = 1)


# In[66]:


type(final_df)


# In[67]:


#printing as a csv locally
final_df.to_csv('files/final_df.csv', index=False)


# In[29]:


final_df


# In[30]:


#setup data split
train_df, test_df = train_test_split(final_df, test_size = 0.5, random_state = 32)


# In[32]:


Y_test = test_df["species"]

X_test = test_df.drop(columns = ["species"], axis = 1)

Y_train = train_df["species"]

X_train = train_df.drop(columns = ["species"], axis = 1)


# In[34]:


#binarize our categorical labels for the species 
final_df["spec_id"] = final_df["species"].factorize()[0]

#setting up the associated dictionary for later usage with heat maps and confusion matrix
spec_id_df = final_df[["species","spec_id"]].drop_duplicates().sort_values("spec_id")


# #### Naive Bayes Classifier

# In[37]:


#set up the model
model_NB = MultinomialNB()


# In[39]:


#fit the model to predict
model_NB.fit(X_train, Y_train)


# In[40]:


#fit the predict
Y_pred_NB = model_NB.predict(X_test)


# In[41]:


#confusion matrix
NB_conf_matrix = confusion_matrix(Y_test, Y_pred_NB)


# In[42]:


NB_conf_matrix


# In[45]:


#call a heatmap
sns.set(color_codes=True)
sns.heatmap(NB_conf_matrix, cmap= "Greens", annot=True, linewidths= 0.5,
           xticklabels = spec_id_df["species"].values, yticklabels = spec_id_df["species"].values)

plt.show()


# In[46]:


print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))


# #### Logistic Regression

# In[47]:


#set up the model
model_log = LogisticRegression(multi_class="multinomial", max_iter=10000)


# In[48]:


#fit the model 
model_log.fit(X_train, Y_train)


# In[50]:


#the model prediction
Y_pred_LOG = model_log.predict(X_test)


# In[51]:


#confusion matrix
LOG_conf_matrix = confusion_matrix(Y_test, Y_pred_LOG)


# In[52]:


#call a heatmap
sns.set(color_codes=True)
sns.heatmap(LOG_conf_matrix, cmap= "Greens", annot=True, linewidths= 0.5,
           xticklabels = spec_id_df["species"].values, yticklabels = spec_id_df["species"].values)

plt.show()


# In[55]:


print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))


# In[54]:


#strong numbers with Logistic Classification
print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))
print(" ")
print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))


# #### K-Nearest Neighbors

# In[56]:


#set up the model
model_KN = KNeighborsClassifier()


# In[57]:


#fit the model
model_KN.fit(X_train,Y_train)


# In[58]:


#set up the predictions
Y_pred_KN = model_KN.predict(X_test)


# In[59]:


#confusion matrix
KN_conf_matrix = confusion_matrix(Y_test, Y_pred_KN)


# In[60]:


#call a heatmap
sns.set(color_codes=True)
sns.heatmap(KN_conf_matrix, cmap= "Greens", annot=True, linewidths= 0.5,
           xticklabels = spec_id_df["species"].values, yticklabels = spec_id_df["species"].values)

plt.show()


# In[61]:


print("Classification Report: KNN")
print(classification_report(Y_test, Y_pred_KN))


# In[63]:


#compare all together..
#strong numbers with Logistic Classification
print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))
print(" ")
print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))
print(" ")
print("Classification Report: KNN")
print(classification_report(Y_test, Y_pred_KN))


# #### SVM (Support Vector Machine)

# In[64]:


#set the model
model_SVC = SVC()


# In[65]:


#fit the model
model_SVC.fit(X_train, Y_train)


# In[68]:


#set up the predictions
Y_pred_SVC = model_SVC.predict(X_test)


# In[69]:


#confusion matrix
SVC_conf_matrix = confusion_matrix(Y_test, Y_pred_SVC)


# In[70]:


#call a heatmap
sns.set(color_codes=True)
sns.heatmap(SVC_conf_matrix, cmap= "Greens", annot=True, linewidths= 0.5,
           xticklabels = spec_id_df["species"].values, yticklabels = spec_id_df["species"].values)

plt.show()


# In[71]:


print("Classification Report: SVC")
print(classification_report(Y_test, Y_pred_SVC))


# In[72]:


#compare all together..
#strong numbers with Logistic Classification
print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))
print(" ")
print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))
print(" ")
print("Classification Report: KNN")
print(classification_report(Y_test, Y_pred_KN))
print(" ")
print("Classification Report: SVC")
print(classification_report(Y_test, Y_pred_SVC))


# #### Random Forest Classifier

# In[74]:


#set up the model
model_RF = RandomForestClassifier()


# In[75]:


#fit the model
model_RF.fit(X_train, Y_train)


# In[76]:


#set up the predictions
Y_pred_RF = model_RF.predict(X_test)


# In[77]:


#confusion matrix
RF_conf_matrix = confusion_matrix(Y_test, Y_pred_RF)


# In[78]:


#call a heatmap
sns.set(color_codes=True)
sns.heatmap(RF_conf_matrix, cmap= "Greens", annot=True, linewidths= 0.5,
           xticklabels = spec_id_df["species"].values, yticklabels = spec_id_df["species"].values)

plt.show()


# In[79]:


print("Classification Report: Random Forest Classifier")
print(classification_report(Y_test, Y_pred_RF))


# In[80]:


#compare all together..
#strong numbers with Logistic Classification
print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))
print(" ")
print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))
print(" ")
print("Classification Report: KNN")
print(classification_report(Y_test, Y_pred_KN))
print(" ")
print("Classification Report: SVC")
print(classification_report(Y_test, Y_pred_SVC))
print(" ")
print("Classification Report: Random Forest Classifier")
print(classification_report(Y_test, Y_pred_RF))


# #### the big three model

# In[81]:


#strong numbers with Logistic Classification
print("Classification Report: Logistic Classification")
print(classification_report(Y_test, Y_pred_LOG))
print(" ")
print("Classification Report: Naive Bayes")
print(classification_report(Y_test, Y_pred_NB))
print(" ")
print("Classification Report: Random Forest Classifier")
print(classification_report(Y_test, Y_pred_RF))


# #### Model Comparison Tool

# In[88]:


#load the csv file with the final_df
df = pd.read_csv('files/final_df.csv')


# In[89]:


final_df


# In[90]:


final_df.columns


# In[92]:


#drop the index 
final_df = df.reset_index(drop=True)


# In[93]:


final_df


# In[94]:


#setup data split (training & test dataframe)
train_df, test_df = train_test_split(final_df, test_size = 0.5, random_state = 32)


# In[95]:


Y_test = test_df["species"]

X_test = test_df.drop(columns = ["species"], axis = 1)

Y_train = train_df["species"]

X_train = train_df.drop(columns = ["species"], axis = 1)


# In[99]:


# Compare the models
# Features
features = X_train.copy()
targets = Y_train.copy()

models = [
    MultinomialNB(),
    LogisticRegression(multi_class="multinomial", max_iter=10000),
    KNeighborsClassifier(),
    SVC(),
    RandomForestClassifier()
]

CV = 5

cv_df = pd.DataFrame(index=range(CV * len(models)))

entries = []

for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, features, targets, scoring="accuracy", cv=CV)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))

cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])


# In[101]:


#visualizing the results
sns.set(color_codes=True)
colors = sns.color_palette("bright")

sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df)
plt.title('Classification Models', fontsize=20)
plt.ylabel('Accuracy', fontsize=15)
plt.xlabel('')
plt.xticks(fontsize=15,rotation=90)
plt.yticks(fontsize=15,rotation=0)
plt.show()


# In[103]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='model_name', y='accuracy', data=cv_df, color='lightblue')
sns.stripplot(x='model_name', y='accuracy', data=cv_df, jitter=True, dodge=True, linewidth=0.5, edgecolor='gray', palette="bright")
plt.title('Classification Models', fontsize=20)
plt.ylabel('Accuracy', fontsize=15)
plt.xlabel('Model', fontsize=15)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()


# In[104]:


#looking at average r squared
final_comp = cv_df.groupby('model_name').accuracy.mean().reset_index().sort_values(by = "accuracy", ascending=False)
final_comp


# #### Model Hyper Tuning & Optimization

# In[105]:


#load the csv file with the final_df
df = pd.read_csv('files/final_df.csv')


# In[106]:


final_df


# In[107]:


final_df.columns


# In[110]:


final_df = df.drop('spec_id', axis=1)


# In[111]:


final_df


# In[112]:


#setup data split (training & test dataframe)
train_df, test_df = train_test_split(final_df, test_size = 0.5, random_state = 32)


# In[113]:


Y_test = test_df["species"]

X_test = test_df.drop(columns = ["species"], axis = 1)

Y_train = train_df["species"]

X_train = train_df.drop(columns = ["species"], axis = 1)


# In[114]:


#doing some optimizations
regressor = MultinomialNB()


# In[118]:


#dictionary grid
grid = {
    "alpha": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "fit_prior": [True, False]
}


# In[119]:


#the model
grid_apply = GridSearchCV(regressor, grid, scoring = "accuracy", cv = 5, refit = True, verbose=2)


# In[120]:


#fit the model
grid_apply.fit(X_train, Y_train)


# In[123]:


#best_performance
best_perf = grid_apply.best_score_

best_model = grid_apply.best_estimator_


# In[124]:


print("Best Accuracy =" + " " + str(best_perf))
print(" ")
print("Best Model Params" + " " + str(best_model))

