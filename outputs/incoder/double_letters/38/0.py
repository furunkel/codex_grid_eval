
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters = ''
    for letter in string:
        if letter == '!':
            double_letters += '!!'
        elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            double_letters += letter * 2
        elif letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters


# Problem 4
def reverse_string(string):
    """
    Given a string, return the string reversed.
    """
    return string[::-1]


# Problem 5
def count_substring(string, substring):
    """
    Given a string and a substring, return the number of times the substring occurs in the string.
    """
    count = 0
    for letter in string:
        if letter == substring:
            count += 1
    return count


# Problem 6
def count_substrings(string, substrings):
    """
    Given a string and a set of substrings, return the number of times the substring occurs in the string.
    """
    count = 0
    for substring in substrings:
        count += count_substring(string, substring)
    return count


# Problem 7
def count_substrings_recursive(string, substrings):
    """
    Given a string and a set of substrings, return the number of times the substring occurs in the string.
    """
    if len(string) == 0:
        return 0
    if len(substrings) == 0:
        return 1
    if string[0] == substrings[0]:
        return 1 + count_substrings_recursive(string[1:], substrings[1:])
    else:
        return count_substrings_recursive(string[1:], substrings[1:])


# Problem 8
def count_substrings_iterative(string, substrings):
    """
    Given a string and a set of substrings, return the number of times the substring occurs in the string.
    """
    count = 0
    substring = substrings[0]
    for letter in string:
        if letter == substring:
            count += 1
            substring = substrings[1:]
    return count


# Problem 9
def count_substrings_recursive2(string, substrings):
    """
    Given a string and a set of substrings, return the number of times the substring occurs in the string.
    """
    if len(string) == 0:
        return 0
    if len(substrings) == 0:
        return 1
    if string[0] == substrings[0]:
        return 1 + count_substrings_recursive2(string[1:], substrings[1:])
    else:
        return count_substrings_recursive2(string[1:], substrings[1:])


# Problem 10
def count_substrings_iterative2(string, substrings):
    """
    Given a string and a set of substrings, return the number of times the substring occurs in the string.
    """
    count = 0
    substring = substrings[0]
    for letter in string:
        if letter == substring:
            count += 1