#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Structure with different data types</font></b></h1></center>

# <center><h1><b><font size="4">Lists</font></b></h1></center>

# In[11]:


list_1 = [0,1,2,3,4,5]
list_2 = ["cat", "dog", "bird", "frog"]


# In[12]:


list_1[0] # 0 position


# In[13]:


list_2[1] # 1 position


# In[14]:


list_2[-2] # -2 position


# In[15]:


list_3 = list_1+list_2


# In[16]:


list_3


# In[17]:


#insert before 1 the string ZERO
list_3[1]="ZERO"
list_3


# In[18]:


list_3[-1] # -1 position


# In[19]:


#reverse
list_1


# In[21]:


list_1.sort(reverse=True)
print(list_1)


# #### new list

# In[22]:


new_list = ["a","b","c","d","e","f"]


# In[23]:


# [a:b] a is included as the first element, and we slice everything before b
new_list[0:1]


# In[24]:


new_list[2:]


# In[25]:


new_list[:]

