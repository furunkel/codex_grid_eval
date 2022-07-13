
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    doubled_string = string
    for letter in string:
        if letter.islower():
            doubled_string = doubled_string.replace(letter, letter*2)
        elif letter == '?':
            doubled_string = doubled_string.replace(letter, letter*3)
    return doubled_string


# In[13]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    doubled_string = string
    for letter in string:
        if letter.islower():
            doubled_string = doubled_string.replace(letter, letter*2)
        elif letter == '?':
            doubled_string = doubled_string.replace(letter, letter*3)
    return doubled_string


# In[14]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    doubled_string = string
    for letter in string:
        if letter.islower():
            doubled_string = doubled_string.replace(letter, letter*2)
        elif letter == '?':
            doubled_string = doubled_string.replace(letter, letter*3)
    return doubled_string


# In[15]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    doubled_string = string
    for letter in string:
        if letter.islower():
            doubled_string = doubled_string.replace(letter, letter*2)
        elif letter == '?':
            doubled_string = doubled_string.replace(letter, letter*3)
    return doubled_string


# In[16]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    doubled_string = string
    for letter in string:
        if letter.islower():
            doubled_string = doubled_string.replace(letter, letter*2)
        elif letter == '?':
            doubled_string = doubled_string.replace(letter, letter*3)
    return doubled_string


# In[17]:


def double_letters_v6(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and 