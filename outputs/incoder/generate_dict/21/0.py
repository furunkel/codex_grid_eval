
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236}

    """
    
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = math.sqrt((i) ** 2)
    return dictionary


# In[11]:


# Test case 1
print(generate_dict(5))


# In[12]:


# Test case 2
print(generate_dict(10))


# In[13]:


# Test case 3
print(generate_dict(100))


# In[14]:


# Test case 4
print(generate_dict(1000))


# In[15]:


# Test case 5
print(generate_dict(10000))


# In[16]:


# Test case 6
print(generate_dict(100000))


# In[17]:


# Test case 7
print(generate_dict(1000000))


# In[18]:


# Test case 8
print(generate_dict(10000000))


# In[19]:


# Test case 9
print(generate_dict(100000000))


# In[20]:


# Test case 10
print(generate_dict(1000000000))


# In[21]:


# Test case 11
print(generate_dict(10000000000))


# In[22]:


# Test case 12
print(generate_dict(100000000000))


# In[23]:


# Test case 13
print(generate_dict(1000000000000))


# In[24]:


# Test case 14
print(generate_dict(10000000000000))


# In[25]:


# Test case 15
print(generate_dict(100000000000000))


# In[26]:


# Test case 16
print(generate_dict(1000000000000000))


# In[27]:


# Test case 17
print(generate_dict(10000000000000000))


# In[28]:


# Test case 18
print(generate_dict(1000000000000000000))


# In[29]:


# Test case 19
print(generate_dict(10000000000000000000))


# In[30]:


# Test case 20
print(generate_dict(100000000000000000000))


# In[31]:


# Test case 21
print(generate_dict(1000000000000000000000))


# In[32]:


# Test case 22
print(generate_dict(10000000000000000000000))


# In[33]:


# Test case 23
print(generate_dict(100000000000000000000000))


# In[34]:


# Test case 24
print(generate_dict(1000000000000000000000000))


# In[35]:


# Test case 25
print(generate_dict(100000000000000000000000000))


# In[36]:


# Test case 26
print(generate_dict(1000000000000000000000000000))


# In[37]:


# Test case 27
print(generate_dict(1000000000000000000000000000000))


