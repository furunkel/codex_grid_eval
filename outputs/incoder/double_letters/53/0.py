
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter in 'aeiou':
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter in '?!':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


# In[11]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter in 'aeiou':
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter in '?!':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


# In[12]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter in 'aeiou':
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter in '?!':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


# In[13]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter in 'aeiou':
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter in '?!':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


# In[14]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter in 'aeiou':
            double_letters_