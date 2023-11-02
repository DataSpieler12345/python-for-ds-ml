#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="6">Function arguments
#     </font></b></h1></center>

# In[3]:


def hello_there(name, greeting="Nice to meet you! How are you doing today?"):
    print("Hello there, "+name+". "+greeting)


# In[4]:


hello_there("Franz")


# In[6]:


hello_there("Franz","what's up?")


# In[7]:


hello_there(greeting= "what's up?", name="bill")


# ### creating a new function 

# In[10]:


def hello_there2(*names):
    for x in names:
        print("Hello there, ",x)


# In[11]:


hello_there2("Franz", "Benny", "Charlie")

