
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 2
        for char in string
        if char.islower()
    )


@register.filter
def triple_caps(string):
    """
    Given a string, return the string, tripling every upper-case letter character, and doubling every lower-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.isupper()
    )


@register.filter
def tripple_letters(string):
    """
    Given a string, return the string, tripling every lower-case letter character, and doubling every upper-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.islower()
    )


@register.filter
def triple_caps_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every lower-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.isupper()
    )


@register.filter
def double_letters_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.islower()
    )


@register.filter
def double_letters_letters_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.isupper()
    )


@register.filter
def triple_caps_letters_letters(string):
    """
    Given a string, return the string, tripling every upper-case letter character, and doubling every lower-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.islower()
    )


@register.filter
def triple_caps_letters_letters_letters(string):
    """
    Given a string, return the string, tripling every upper-case letter character, and doubling every lower-case letter character.
    All other characters should be output a single time each.
    """
    return ''.join(
        char * 3
        for char in string
        if char.isupper()