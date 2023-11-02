#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Structure with different data types</font></b></h1></center>

# <center><h1><b><font size="4">Sets</font></b></h1></center>

# In[2]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}


# In[3]:


#listing all item existing in A or B
A|B


# In[5]:


A.union(B)


# In[6]:


B.union(A)


# In[7]:


A&B


# In[8]:


A-B


# In[9]:


A


# In[10]:


B


# In[12]:


B-A

