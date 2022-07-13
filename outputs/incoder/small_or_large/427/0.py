
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "house" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return "none"


# In[13]:


def count_letters(n):
    """
        Given an integer n, return the number of letters in the English alphabet.
    """
    count = 0
    for i in range(26):
        if n % 26 == i:
            count += 1
    return count


# In[14]:


def count_digits(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[15]:


def count_digits_string(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[16]:


def count_digits_string2(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[17]:


def count_digits_string3(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[18]:


def count_digits_string4(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[19]:


def count_digits_string5(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[20]:


def count_digits_string6(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n > 0:
        n /= 10
        count += 1
    return count


# In[21]:


def count_digits_string7(n):
    """
        Given an integer n, return the number of digits in n. Assume that n has only digits and no letters.
    """
    count = 0
    while n 