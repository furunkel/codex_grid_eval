
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter == "!":
            double_letters += "!!"
        elif letter == "?":
            double_letters += "??"
        elif letter in ["a", "e", "i", "o", "u"]:
            double_letters += letter * 2
        elif letter in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters


# In[14]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter == "!":
            double_letters += "!!"
        elif letter == "?":
            double_letters += "??"
        elif letter in ["a", "e", "i", "o", "u"]:
            double_letters += letter * 2
        elif letter in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters


# In[15]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter == "!":
            double_letters += "!!"
        elif letter == "?":
            double_letters += "??"
        elif letter in ["a", "e", "i", "o", "u"]:
            double_letters += letter * 2
        elif letter in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters


# In[16]:


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every exclamation point charact