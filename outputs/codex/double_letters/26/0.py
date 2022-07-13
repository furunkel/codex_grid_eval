
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.islower():
            result += char * 2
        elif char.isupper():
            result += char * 3
        else:
            result += char
    return result


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char * 2
            else:
                result += char * 3
        else:
            result += char
    return result


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isalpha():
            result += char * (2 if char.islower() else 3)
        else:
            result += char
    return result


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isalpha():
            result += char * (2 if char.islower() else 3)
        else:
            result += char
    return result


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isalpha():
            result += char * (2 if char.islower() else 3)
        else:
            result += char
    return result


def double_letters_v6(string):
    """