
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in questions:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in questions:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in questions:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in questions:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter
    return double_letters_string


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = ""
    for letter in string:
        if letter in consonants:
            double_letters_string += letter * 2
        elif letter in questions:
            double_letters_string += letter * 3
        else:
            double_letters_string += letter