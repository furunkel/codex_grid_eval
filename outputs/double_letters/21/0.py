
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char * 2
        elif char == "?":
            new_string += char * 3
        else:
            new_string += char
    return new_string


def is_palindrome(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    return string == string[::-1]


def is_palindrome_v2(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def is_palindrome_v3(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


def is_palindrome_v4(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


def is_palindrome_v5(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


def is_palindrome_v6(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
    """
    return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


def is_palindrome_v7(string):
    """
    Given a string, return True if the string is a palindrome, and False otherwise.
