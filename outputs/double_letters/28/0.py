
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char * 2
        elif char == "!":
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_v2(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char * 2
        elif char == "!":
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_v3(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char * 2
        elif char == "!":
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_v4(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char * 2
        elif char == "!":
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_v5(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.isl