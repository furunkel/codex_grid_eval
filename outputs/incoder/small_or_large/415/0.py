
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "house" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return None


# In[14]:


def count_words(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = text.count(word)
    return counts


# In[15]:


def count_words_regex(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[16]:


def count_words_regex_multi(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[17]:


def count_words_regex_multi2(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[18]:


def count_words_regex_multi3(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[19]:


def count_words_regex_multi4(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[20]:


def count_words_regex_multi5(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = len(re.findall(word, text))
    return counts


# In[21]:


def count_words_regex_multi6(text, words):
    """
        Count the number of occurrences of all the words in `words` in `text`.
    """
    words = words.split()
    counts = {}
    for word in words:
        counts[word] = 