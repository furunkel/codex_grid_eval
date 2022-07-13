
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    double_vowels = []
    double_consonants = []
    for letter in string:
        if letter in vowels:
            double_vowels.append(letter)
        elif letter in consonants:
            double_consonants.append(letter)
        else:
            double_vowels.append(letter)
            double_consonants.append(letter)
    return ''.join(double_vowels) + '{}{}{}'.format(*double_consonants)


# In[17]:


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    double_vowels = []
    double_consonants = []
    for letter in string:
        if letter in vowels:
            double_vowels.append(letter)
        elif letter in consonants:
            double_consonants.append(letter)
        else:
            double_vowels.append(letter)
            double_consonants.append(letter)
    return ''.join(double_vowels) + '{}{}{}'.format(*double_consonants)


# In[18]:


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    double_vowels = []
    double_consonants = []
    for letter in string:
        if letter in vowels:
            double_vowels.append(letter)
        elif letter in consonants:
            double_consonants.append(letter)
        else:
            double_vowels.append(letter)
            double_consonants.append(letter)
    return ''.join(double_vowels) + '{}{}{}'.format(*double_consonants)


# In