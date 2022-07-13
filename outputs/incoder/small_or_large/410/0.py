
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "house" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
        return "house"
    else:
        return None


# In[14]:


def count_words(text, words):
    """
        Count the number of times each word appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[15]:


def count_words_bigram(text, words):
    """
        Count the number of times each bigram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[16]:


def count_words_trigram(text, words):
    """
        Count the number of times each trigram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[17]:


def count_words_fourgram(text, words):
    """
        Count the number of times each fourgram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[18]:


def count_words_fivegram(text, words):
    """
        Count the number of times each fivegram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[19]:


def count_words_sixgram(text, words):
    """
        Count the number of times each sixgram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[20]:


def count_words_sevengram(text, words):
    """
        Count the number of times each sevengram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[21]:


def count_words_eightgram(text, words):
    """
        Count the number of times each eightgram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[22]:


def count_words_ninegram(text, words):
    """
        Count the number of times each ninegram appears in a text.
    """
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[23]:


def count_words_tengram(text, words):
    """
