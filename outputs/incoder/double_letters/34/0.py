
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    double_letters_re = re.compile(r"!|@|#|$|%|&|*|(|)|-|_|+|\?|/|:|;|<|>|=|,|\.|\[|\]|\{|\}|\^|_|`|\{|\}|~")
    return double_letters_re.sub(r"\1\1\1", string)


@register.filter
def remove_special_characters(string):
    """
    Given a string, remove all special characters, including spaces, commas, and periods.
    """
    special_characters_re = re.compile(r"[!,@,#,$,%,&,*,(,),-,_,+,?,/:;<=>?@\[\\\]^_`{|}~]")
    return special_characters_re.sub("", string)


@register.filter
def remove_spaces(string):
    """
    Given a string, remove all spaces.
    """
    spaces_re = re.compile(r"\s+")
    return spaces_re.sub("", string)


@register.filter
def remove_newlines(string):
    """
    Given a string, remove all newlines.
    """
    newlines_re = re.compile(r"\n")
    return newlines_re.sub("", string)


@register.filter
def remove_hyphens(string):
    """
    Given a string, remove all hyphens.
    """
    hyphens_re = re.compile(r"-")
    return hyphens_re.sub("", string)


@register.filter
def remove_apostrophes(string):
    """
    Given a string, remove all apostrophes.
    """
    apostrophes_re = re.compile(r"'")
    return apostrophes_re.sub("", string)


@register.filter
def remove_hyphens_and_apostrophes(string):
    """
    Given a string, remove all hyphens and apostrophes.
    """
    hyphens_and_apostrophes_re = re.compile(r"-|\'")
    return hyphens_and_apostrophes_re.sub("", string)


@register.filter
def remove_multiple_spaces(string):
    """
    Given a string, remove all multiple spaces.
    """
    multiple_spaces_re = re.compile(r"\s+")
    return multiple_spaces_re.sub(" ", string)


@register.filter
def remove_multiple_newlines(string):
    """
    Given a string, remove all multiple newlines.
    """
    multiple_newlines_re = re.compile(r"\n")
    return multiple_newlines_re.sub("", string)


@register.filter
def remove_multiple_hyphens(string):
    """
    Given a string, remove all multiple hyphens.
    """
    multiple_hyphens_re = re.compile(r"-")
    return multiple_