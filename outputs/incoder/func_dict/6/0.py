
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    
    dictionary = {}
    
    for i in range(1, n + 1):
        
        if i in dictionary:
            dictionary[i] = dictionary[i - 1]
        else:
            dictionary[i] = i - 1
            
    return dictionary


# In[11]:


# Test your code
dictionary = generate_dict(10)
print(dictionary)


# In[12]:


# Test your code
dictionary = generate_dict(100)
print(dictionary)


# In[13]:


# Test your code
dictionary = generate_dict(1000)
print(dictionary)


# In[14]:


# Test your code
dictionary = generate_dict(10000)
print(dictionary)


# In[15]:


# Test your code
dictionary = generate_dict(100000)
print(dictionary)


# In[16]:


# Test your code
dictionary = generate_dict(1000000)
print(dictionary)


# In[17]:


# Test your code
dictionary = generate_dict(10000000)
print(dictionary)


# In[18]:


# Test your code
dictionary = generate_dict(100000000)
print(dictionary)


# In[19]:


# Test your code
dictionary = generate_dict(1000000000)
print(dictionary)


# In[20]:


# Test your code
dictionary = generate_dict(10000000000)
print(dictionary)


# In[21]:


# Test your code
dictionary = generate_dict(100000000000)
print(dictionary)


# In[22]:


# Test your code
dictionary = generate_dict(1000000000000)
print(dictionary)


# In[23]:


# Test your code
dictionary = generate_dict(1000000000001)
print(dictionary)


# In[24]:


# Test your code
dictionary = generate_dict(1000000000002)
print(dictionary)


# In[25]:


# Test your code
dictionary = generate_dict(1000000000003)
print(dictionary)


# In[26]:


# Test your code
dictionary = generate_dict(1000000000004)
print(dictionary)


# In[27]:


# Test your code
dictionary = generate_dict(1000000000005)
print(dictionary)


# In[28]:


# Test your code
dictionary = generate_dict(1000000000006)
print(dictionary)


# In[29]:


# Test your code
dictionary = generate_dict(1000000000007)
print(dictionary)


# In[30]:


# Test your code
dictionary = generate_dict(1000000000008)
print(dictionary)


# In[31]:


# Test your code
dictionary = generate_