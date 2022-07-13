
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "large" if n >= 15 (and None if 2 <= n < 15).
    """
    if n < 2:
        return "mouse"
    if n >= 15:
        return "large"
    return None


# In[14]:


def count_small_or_large(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        count += small_or_large(n)
    return count


# In[15]:


def count_small_or_large_2(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse":
            count += 1
    return count


# In[16]:


def count_small_or_large_3(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "large":
            count += 1
    return count


# In[17]:


def count_small_or_large_4(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse" or small_or_large(n) == "large":
            count += 1
    return count


# In[18]:


def count_small_or_large_5(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse" or small_or_large(n) == "large":
            count += 1
    return count


# In[19]:


def count_small_or_large_6(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse" or small_or_large(n) == "large":
            count += 1
    return count


# In[20]:


def count_small_or_large_7(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse" or small_or_large(n) == "large":
            count += 1
    return count


# In[21]:


def count_small_or_large_8(numbers):
    """
        Count the number of "mouse" and "large" in the list of numbers.
    """
    count = 0
    for n in numbers:
        if small_or_large(n) == "mouse" or small_or_large(n) == "large":
            count += 1
    return count


# In[22]:


def count_small_or_large_9(numbers):
    """
        Coun