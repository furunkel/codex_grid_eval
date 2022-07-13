
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 1000 and "house" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n >= 2000:
        return "house"
    else:
        return None


# In[14]:


def count_houses(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 - 1
    else:
        return None


# In[15]:


def count_houses_v2(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000
    else:
        return None


# In[16]:


def count_houses_v3(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 1
    else:
        return None


# In[17]:


def count_houses_v4(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 2
    else:
        return None


# In[18]:


def count_houses_v5(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 3
    else:
        return None


# In[19]:


def count_houses_v6(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 4
    else:
        return None


# In[20]:


def count_houses_v7(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 5
    else:
        return None


# In[21]:


def count_houses_v8(n):
    """
        Given an integer n, return how many houses there are in the houses comprising n houses.
    """
    if n < 1000:
        return 0
    elif n >= 2000:
        return n // 1000 + 6
    else:
        return None


# In[22]:


def count_houses_v