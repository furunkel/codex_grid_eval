
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_result = ''
    for letter in string:
        if letter.isdigit():
            double_letters_result += letter * 2
        elif letter == '?':
            double_letters_result += letter * 3
        else:
            double_letters_result += letter
    return double_letters_result


def double_letters_recursive(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    if len(string) <= 1:
        return string
    else:
        return double_letters_recursive(string[1:]) + string[0]


def double_letters_iterative(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_result = ''
    for letter in string:
        if letter.isdigit():
            double_letters_result += letter * 2
        elif letter == '?':
            double_letters_result += letter * 3
        else:
            double_letters_result += letter
    return double_letters_result


def double_letters_recursion_iterative(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    if len(string) <= 1:
        return string
    else:
        return double_letters_recursion_iterative(string[1:]) + string[0]


def double_letters_iterative_recursive(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_result = ''
    for letter in string:
        if letter.isdigit():
            double_letters_result += letter * 2
        elif letter == '?':
            double_letters_result += letter * 3
        else:
            double_letters_result += letter
    return double_letters_result


def double_letters_recursion_iterative_recursive(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    if len(string) <= 1:
        return string
    else:
        return double_letters_recursion_iterative_recursive(string[1:]) + string[0]


def double_letters_iterative_recursive_iterative(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_result = ''