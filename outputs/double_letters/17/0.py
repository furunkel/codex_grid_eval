
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every number.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char * 2
        elif char.isdigit():
            result += char * 3
        else:
            result += char
    return result


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
    """
    return all(string[