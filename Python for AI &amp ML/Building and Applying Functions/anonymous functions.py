#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Anonymous functions</font></b></h1></center>

# In[1]:


double = lambda x:x*2


# In[2]:


double(5)


# In[3]:


double(-5)


# ### creating a function

# In[4]:


def doubler(number):
    return number*2          


# In[6]:


doubler(5)


# In[7]:


doubler(-5)


# ### creating a another function

# In[8]:


my_list = [1,4,5,6,7,19]

new_list = list(filter(lambda x:(x%2 == 0), my_list))

print(new_list)


# In[9]:


my_list = [1,4,5,6,7,19]

new_list = list(filter(lambda x:x**2, my_list))

print(new_list)


# In[10]:


my_list = [1,4,5,6,7,19]

new_list = list(map(lambda x:x**2, my_list))

print(new_list)

