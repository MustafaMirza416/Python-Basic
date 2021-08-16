#!/usr/bin/env python
# coding: utf-8

# # Boolean
# 

# In[1]:


print(True,False)


# In[2]:


type(True)


# In[3]:


type(False)


# In[17]:


my_str="Mirza"


# In[18]:


my_str


# In[19]:


type(my_str)


# In[20]:


my_str.isalnum()


# # Boolean and Logical Operators

# In[21]:


True and True


# In[22]:


True and False


# In[24]:


True or False


# In[25]:


True or True


# In[26]:


str1="Hello World"
my_str="Mirza"


# In[27]:


my_str.isalpha() or str1.isnum


# # List

# In[28]:


lst = []


# In[29]:


type(lst)


# In[30]:


lst = ['Math','chemistry',100,200,300]


# In[31]:


type(lst)


# # Append

# In[47]:


#append is used to add elements in the list
#append add the elements at the last


# In[33]:


lst.append("physics")


# In[34]:


lst


# In[46]:


lst.append(["mirza","baig"])
#its form like nested list not append
#


# In[44]:


lst


# # Insert

# In[35]:


#insert in a specific order


# In[36]:


lst.insert(3,500)


# In[37]:


lst


# # Indexing
# 

# In[38]:


lst[:]


# In[39]:


lst[1:]


# In[40]:


lst[2:5]


# In[41]:


lst[:5]


# In[42]:


len(lst)


# # Extend

# In[51]:


lst1=[1,2,3,4,5,6,7]
# multiple elements added not like append


# In[52]:


lst1.extend([8,9])


# In[53]:


lst1


# # Various Operations That we can perform in list

# In[75]:


lst=[1,2,3,4,5]


# In[76]:


sum(lst)


# In[77]:


lst*2


# # Pop()
# 

# In[59]:


#Default removes last element


# In[57]:


lst.pop()


# In[58]:


lst


# In[60]:


lst.pop(0)


# In[61]:


lst


# # count

# In[66]:


lst=[1,1,3,4,1,4,4]


# In[68]:


lst.count(1)


# In[70]:


lst.count(4)


# In[71]:


min(lst)


# In[72]:


max(lst)


# In[ ]:




