
def double_letters(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "?":
            new_string += "???"
        else:
            new_string += char * 2
    return new_string


def double_letters_2(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "?":
            new_string += "???"
        elif char.isalpha():
            new_string += char * 2
        else:
            new_string += char
    return new_string


def double_letters_3(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "?":
            new_string += "???"
        elif char.isalpha():
            new_string += char * 2
        else:
            new_string += char
    return new_string


def double_letters_4(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "?":
            new_string += "???"
        elif char.isalpha():
            new_string += char * 2
        else:
            new_string += char
    return new_string


def double_letters_5(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "?":
            new_string += "???"
        elif char.isalpha():
            new_string += char * 2
        else:
            new