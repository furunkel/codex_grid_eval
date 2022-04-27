
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    new_string = ""
    for char in string:
        if char in vowels:
            new_string += char * 3
        elif char in consonants:
            new_string += char * 2
        else:
            new_string += char
    return new_string

def double_letters_2(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    new_string = ""
    for char in string:
        if char in vowels:
            new_string += char * 3
        elif char in consonants:
            new_string += char * 2
        else:
            new_string += char
    return new_string

def double_letters_3(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    new_string = ""
    for char in string:
        if char in vowels:
            new_string += char * 3
        elif char in consonants:
            new_string += char * 2
        else:
            new_string += char
    return new_string

def double_letters_4(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-