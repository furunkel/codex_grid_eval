
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""
    for char in string:
        if char in vowels:
            result += char * 2
        elif char in consonants:
            result += char * 3
        else:
            result += char
    return result

def double_letters_regex(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""
    for char in string:
        if char in vowels:
            result += char * 2
        elif char in consonants:
            result += char * 3
        else:
            result += char
    return result

def double_letters_regex(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""
    for char in string:
        if char in vowels:
            result += char * 2
        elif char in consonants:
            result += char * 3
        else:
            result += char
    return result

def double_letters_regex(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a