
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter.isupper():
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter == '?':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


@register.filter
def double_letters_reverse(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter.islower():
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter == '?':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


@register.filter
def double_letters_reverse2(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter.islower():
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter == '?':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


@register.filter
def double_letters_reverse3(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter.islower():
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter == '?':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


@register.filter
def double_letters_reverse4(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    double_letters_string = string
    for letter in string:
        if letter.islower():
            double_letters_string = double_letters_string.replace(letter, letter * 2)
        if letter == '?':
            double_letters_string = double_letters_string.replace(letter, letter * 3)
    return double_letters_string


@register.filter
def double_letters_reverse