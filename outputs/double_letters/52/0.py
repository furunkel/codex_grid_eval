
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char in vowels:
            result += char * 2
        elif char == "!":
            result += char * 3
        else:
            result += char
    return result

def double_letters_regex(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU])', r'\1\1', re.sub(r'(!)', r'\1\1\1', string))

def double_letters_regex_2(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|!)', lambda m: m.group(1) * 2 if m.group(1) != "!" else m.group(1) * 3, string)

def double_letters_regex_3(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|!)', lambda m: m.group(1) * (3 if m.group(1) == "!" else 2), string)

def double_letters_regex_4(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return re.sub(r'([aeiouAEIOU]|!)', lambda m: m.group(1) * (3 if m.group(1) ==