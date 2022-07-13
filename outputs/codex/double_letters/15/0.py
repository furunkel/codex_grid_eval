
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() in "aeiou":
                result += char
            else:
                result += char * 3
        elif char.isdigit():
            result += char * 2
        else:
            result += char
    return result


def double_letters_regex(string):
    """
    Given a string, return the string, doubling every number character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|\d)', lambda m: m.group(1) * 2 if m.group(1).isdigit() else m.group(1) * 3, string)


def double_letters_regex_2(string):
    """
    Given a string, return the string, doubling every number character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|\d)', lambda m: m.group(1) * (3 if m.group(1).isalpha() else 2), string)


def double_letters_regex_3(string):
    """
    Given a string, return the string, doubling every number character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|\d)', lambda m: m.group(1) * (3 if m.group(1).isalpha() else 2), string)


def double_letters_regex_4(string):
    """
    Given a string, return the string, doubling every number character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|\d)', lambda m: m.group(