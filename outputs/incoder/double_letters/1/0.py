
def double_letters(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isalpha():
            double_letters += letter * 2
        elif letter.isdigit():
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters


def double_digits(string):
    """
    Given a string, return the string, doubling every digit character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_digits = ""
    for digit in string:
        if digit.isdigit():
            double_digits += digit * 2
        elif digit.isalpha():
            double_digits += digit * 3
        else:
            double_digits += digit
    return double_digits


def double_digits_and_letters(string):
    """
    Given a string, return the string, doubling every digit character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_digits_and_letters = ""
    for digit in string:
        if digit.isdigit():
            double_digits_and_letters += digit * 2
        elif digit.isalpha():
            double_digits_and_letters += digit * 3
        else:
            double_digits_and_letters += digit
    return double_digits_and_letters


def double_digits_and_letters_and_spaces(string):
    """
    Given a string, return the string, doubling every digit character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_digits_and_letters_and_spaces = ""
    for digit in string:
        if digit.isdigit():
            double_digits_and_letters_and_spaces += digit * 2
        elif digit.isalpha():
            double_digits_and_letters_and_spaces += digit * 3
        else:
            double_digits_and_letters_and_spaces += digit
    return double_digits_and_letters_and_spaces


def double_digits_and_letters_and_spaces_and_numbers(string):
    """
    Given a string, return the string, doubling every digit character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_digits_and_letters_and_spaces_and_numbers = ""
    for digit in string:
        if digit.isdigit():
            double_digits_and_letters_and_spaces_and_numbers += digit * 2
        elif digit.isalpha():
            double_digits_and_letters_and_spaces_and_numbers += digit * 3
        else:
            double_digits_and_letters_and_spaces_and_numbers += digit
    return double_digits_and_letters_and_spaces_and_numbers


def double_digits_and_letters_and_spaces_and_numbers_and_punctuation(string):
    """
    Given a string, return the string, doubling every digit character, and tripling every number.