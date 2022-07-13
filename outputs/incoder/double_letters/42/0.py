
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster_2(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster_3(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster_4(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster_5(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return re.sub(r"\?+", lambda match: match.group() * 2, string).replace(
        lambda match: match.group().upper(), lambda match: match.group().upper()
    )


@lru_cache(maxsize=1024)
def double_letters_faster_6(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every 