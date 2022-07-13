
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = ""
    for char in string:
        if char in vowels:
            result += char
        elif char in consonants:
            result += char * 2
        elif char == "?":
            result += char * 3
        else:
            result += char
    return result


def double_letters_regex(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return re.sub(r'([bcdfghjklmnpqrstvwxyz])', r'\1\1', re.sub(r'\?', r'???', string))


def double_letters_regex_2(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return re.sub(r'([bcdfghjklmnpqrstvwxyz]|\?)', r'\1\1\1', string)


def double_letters_regex_3(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return re.sub(r'([bcdfghjklmnpqrstvwxyz]|\?)', lambda m: m.group(1) * 3, string)


def double_letters_regex_4(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return re.sub(r'([bcdfghjklmnpqrstvw