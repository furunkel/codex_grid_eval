
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter == "?":
            double_letters_string += "?"
        elif letter in "aeiouAEIOU":
            double_letters_string += letter * 2
        else:
            double_letters_string += letter
    return double_letters_string


# In[11]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter == "?":
            double_letters_string += "?"
        elif letter in "aeiouAEIOU":
            double_letters_string += letter * 2
        else:
            double_letters_string += letter
    return double_letters_string


# In[12]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter == "?":
            double_letters_string += "?"
        elif letter in "aeiouAEIOU":
            double_letters_string += letter * 2
        else:
            double_letters_string += letter
    return double_letters_string


# In[13]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter == "?":
            double_letters_string += "?"
        elif letter in "aeiouAEIOU":
            double_letters_string += letter * 2
        else:
            double_letters_string += letter
    return double_letters_string


# In[14]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter == "?":
            double_letters_string += "?"
        elif letter in "aeiouAEIOU":