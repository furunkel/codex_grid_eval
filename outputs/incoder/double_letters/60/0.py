
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in exclamation_points:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


# In[14]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in exclamation_points:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


# In[15]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in exclamation_points:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


# In[16]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in exclamation_points:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


# In[17]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letter