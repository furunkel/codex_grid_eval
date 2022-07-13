
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter
        elif letter == "!":
            double_letters += letter
        else:
            double_letters += letter
            double_letters += letter
    return double_letters


# In[14]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter
        elif letter == "!":
            double_letters += letter
        else:
            double_letters += letter
            double_letters += letter
            double_letters += letter
    return double_letters


# In[15]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter
        elif letter == "!":
            double_letters += letter
        else:
            double_letters += letter
            double_letters += letter
            double_letters += letter
            double_letters += letter
    return double_letters


# In[16]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter
        elif letter == "!":
            double_letters += letter
        else:
            double_letters += letter
            double_letters += letter
            double_letters += letter
            double_letters += letter
            double_letters += letter
    return double_letters


# In[17]:


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter
        elif letter == "!":
            double_letters += letter
        else:
            double_letters += letter
            double_letters += letter
            double_