
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 15 (and neither if -100 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= 15:
        return "house"
    else:
        return "none"


# In[14]:


def count_words(text):
    """
        Count the number of words in text.
    """
    words = text.split()
    return len(words)


# In[15]:


def count_characters(text):
    """
        Count the number of characters in text.
    """
    characters = len(text)
    return characters


# In[16]:


def count_syllables(text):
    """
        Count the number of syllables in text.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables(word)
    return syllables


# In[17]:


def count_syllables_simple(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple(word)
    return syllables


# In[18]:


def count_syllables_simple2(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple2(word)
    return syllables


# In[19]:


def count_syllables_simple3(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple3(word)
    return syllables


# In[20]:


def count_syllables_simple4(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple4(word)
    return syllables


# In[21]:


def count_syllables_simple5(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple5(word)
    return syllables


# In[22]:


def count_syllables_simple6(text):
    """
        Count the number of syllables in text using only letters.
    """
    syllables = 0
    words = text.split()
    for word in words:
        syllables += count_syllables_simple6(word)
    return syllables


# In[23]:


def count_syllables_simple7(text):
    """
        Count the number of syllables in text using only letters.
    """
    