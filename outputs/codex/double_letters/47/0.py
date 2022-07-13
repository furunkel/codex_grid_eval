
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char == "?":
            result += "??"
        elif char.isalpha() and char not in "aeiouAEIOU":
            result += char * 3
        else:
            result += char
    return result


def double_letters_regex(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'\?', '??', re.sub(r'[^aeiouAEIOU]', lambda x: x.group() * 3, string))


def double_letters_regex_2(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'\?', '??', re.sub(r'[^aeiouAEIOU]', lambda x: x.group() * 3, string))


def double_letters_regex_3(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'\?', '??', re.sub(r'[^aeiouAEIOU]', lambda x: x.group() * 3, string))


def double_letters_regex_4(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'\?', '??', re.sub(r'[^aeiouAEIOU]', lambda x: x.group() * 3, string))


def double_letters_regex_5(string):
    """
