
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_rev_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev_inverse(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_inverse_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_rev_inverse_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev_inverse_2(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_inverse_2_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_rev_inverse_2_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev_inverse_3(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_inverse_3_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_rev_inverse_3_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev_inverse_4(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_inverse_4_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_letters_rev_inverse_4_re.sub(lambda match: match.group(1) * 2, string)


def double_letters_rev_inverse_5(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    double_letters_rev_inverse_5_re = re.compile(r"(.)\1*", re.DOTALL)
    return double_