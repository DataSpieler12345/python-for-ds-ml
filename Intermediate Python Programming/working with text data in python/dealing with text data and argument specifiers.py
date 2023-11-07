#!/usr/bin/env python
# coding: utf-8

# <center><h1><b><font size="5">Dealing with Text Data and Argument Specifiers</font></b></h1></center>

# In[1]:


product_category = 'A'
print('This item is from product category "%s".' % product_category)


# In[2]:


product_category = 'B'
print('This item is from product category "%s".' % product_category)


# In[3]:


#list string values
product_category = ['A','B']
print('This item is from product category "%s".' % product_category)


# In[4]:


#list string values
product_category = ['A','B']
print('This item is from product category "%s".' % product_category[0])


# In[5]:


#list string values
product_category = ['A','B']
print('This item is from product category "%s".' % product_category[1])


# #### another example

# In[6]:


quantities = [500,600]
print('This item is from product category "%s".' % quantities[1])


# In[7]:


quantities = [500,600]
print('This item is from product category "%s".' % quantities[0])


# In[8]:


print("We currently have %d available units of this item." % quantities[0])


# In[9]:


print("We currently have %d available units of this item." % quantities[1])


# #### another example

# In[10]:


stock_share_price_list = [40.50,6.35]
print("This stock costs $%.2f per share." % stock_share_price_list[1])


# In[11]:


stock_share_price_list = [40.50,6.35]
print("This stock costs $%.2f per share." % stock_share_price_list[0])


# In[14]:


i = 0
print("Currently, we have %d units of category \"%s\" products in store." % (quantities[i], product_category[i]))

