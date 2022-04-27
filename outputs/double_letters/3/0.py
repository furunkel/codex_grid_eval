
def double_letters(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() in vowels:
                result += char * 2
            else:
                result += char * 3
        else:
            result += char
    return result


def double_letters_2(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() in vowels:
                result += char * 2
            else:
                result += char * 3
        else:
            result += char
    return result


def double_letters_3(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() in vowels:
                result += char * 2
            else:
                result += char * 3
        else:
            result += char
    return result


def double_letters_4(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() in vowels:
                result += char * 2
            else:
                result += char * 3
        else:
            result += char
    return result


def double_letters_5(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every consonant (lower-case or upper-case).