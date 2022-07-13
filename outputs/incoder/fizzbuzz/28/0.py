
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 23 (instead of the number),
        "FizzBuzz" for multiples of both three and 23  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 23 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 23 == 0:
        return "Buzz"
    else:
        return num


# In[17]:


# Test your code
fizzbuzz(15)


# In[18]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(15)


# In[19]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(99)


# In[20]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(100)


# In[21]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(101)


# In[22]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(102)


# In[23]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(103)


# In[24]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(104)


# In[25]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(105)


# In[26]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(106)


# In[27]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(107)


# In[28]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(108)


# In[29]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(109)


# In[30]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(110)


# In[31]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(111)


# In[32]:


# Experiment with different inputs to .fizzbuzz()
fizzbuzz(112)


# In[33