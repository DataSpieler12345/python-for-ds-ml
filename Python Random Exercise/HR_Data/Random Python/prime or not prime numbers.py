#!/usr/bin/env python
# coding: utf-8

# ### Create a Function to Check if a Number Is Prime

# In[1]:


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# ### Test the function

# In[2]:


is_prime(1)


# In[3]:


is_prime(2)


# In[4]:


is_prime(3)


# In[5]:


is_prime(4)


# In[6]:


is_prime(5)


# In[7]:


is_prime(6)


# In[8]:


is_prime(7)


# In[9]:


is_prime(8)


# In[10]:


is_prime(9)


# In[11]:


is_prime(10)


# In[12]:


is_prime(11)


# In[13]:


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

count = 0

for num in range(100, 152):
    if is_prime(num):
        count += 1

print("The number of prime numbers in the range from 100 to 151 is:", count)


# In[14]:


is_prime(123)


# In[15]:


is_prime(827)


# In[16]:


is_prime(326)


# In[17]:


is_prime(303)


# In[18]:


is_prime(313)


# In[19]:


is_prime(351)

