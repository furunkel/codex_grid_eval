
def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(lst, key=lambda t: t[1])[0]


# In[11]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)])
print(result)


# In[12]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1])
print(result)


# In[13]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True)
print(result)


# In[14]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[15]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[16]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[17]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[18]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[19]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[20]:


# Test your function
result = f([('Bob', 75), ('Alice', 60), ('Fred', 55), ('Bob', 85), ('Alice', 100)], key=lambda t: t[1], reverse=True, key=lambda x: -x[1])
print(result)


# In[2