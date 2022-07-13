
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "house" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return "house"


# In[14]:


def count_houses(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    if n < 10:
        return 0
    elif n >= 2000:
        return 1
    else:
        return count_houses(n // 10) + 1


# In[15]:


def count_houses_recursive(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    if n < 10:
        return 0
    elif n >= 2000:
        return 1
    else:
        return count_houses_recursive(n // 10) + 1


# In[16]:


def count_houses_iterative(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    count = 0
    while n >= 10:
        count += 1
        n //= 10
    return count


# In[17]:


def count_houses_memoization(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    memo = {}
    if n in memo:
        return memo[n]
    if n < 10:
        memo[n] = 0
    elif n >= 2000:
        memo[n] = 1
    else:
        memo[n] = count_houses_memoization(n // 10) + 1
    return memo[n]


# In[18]:


def count_houses_memoization_iterative(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    memo = {}
    count = 0
    while n >= 10:
        if n in memo:
            count += 1
            n //= 10
        else:
            memo[n] = count_houses_memoization(n // 10) + 1
            count += 1
    return count


# In[19]:


def count_houses_memoization_iterative_recursive(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    memo = {}
    count = 0
    if n in memo:
        return memo[n]
    if n < 10:
        memo[n] = 0
    elif n >= 2000:
        memo[n] = 1
    else:
        memo[n] = count_houses_memoization_iterative_recursive(n // 10) + 1
        count += 1
    return memo[n]


# In[20]:


def count_houses_memoization_iterative_recursive_recursive(n):
    """
        Given an integer n, return the number of houses there are in the house.
    """
    memo = {}
    count = 0
    if n in memo:
        return memo[n]
    if n < 