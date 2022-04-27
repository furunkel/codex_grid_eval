
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    vowels = "aeiou"
    result = ""
    for char in string:
        if char.isalpha() and char.lower() not in vowels:
            result += char * 2
        elif char.isdigit():
            result += char * 3
        else:
            result += char
    return result


def double_letters_regex(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    return re.sub(r'([^aeiouAEIOU0-9])', r'\1\1', string)


def double_letters_regex_2(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    return re.sub(r'([^aeiouAEIOU0-9])', r'\1\1', re.sub(r'([0-9])', r'\1\1\1', string))


def double_letters_regex_3(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    return re.sub(r'([^aeiouAEIOU0-9]|[0-9])', r'\1\1\1', string)


def double_letters_regex_4(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    return re.sub(r'([^aeiouAEIOU0-9]|[0-9])', lambda m: m.group(1) * 2 if m.group(1).isalpha() else m.group(1) * 3,