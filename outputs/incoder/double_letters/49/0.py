
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char in 'aeiou':
            double_letters_string += char * 2
        elif char in '1234567890':
            double_letters_string += char * 3
        else:
            double_letters_string += char
    return double_letters_string


# In[14]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char in 'aeiou':
            double_letters_string += char * 2
        elif char in '1234567890':
            double_letters_string += char * 3
        else:
            double_letters_string += char
    return double_letters_string


# In[15]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char in 'aeiou':
            double_letters_string += char * 2
        elif char in '1234567890':
            double_letters_string += char * 3
        else:
            double_letters_string += char
    return double_letters_string


# In[16]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char in 'aeiou':
            double_letters_string += char * 2
        elif char in '1234567890':
            double_letters_string += char * 3
        else:
            double_letters_string += char
    return double_letters_string


# In[17]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char in 'aeiou':
            double_letters_string += char * 2
        elif char in '1234567890':
            double_letters_string += char * 3
        else:
            double_letters_string 