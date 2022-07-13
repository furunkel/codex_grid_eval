
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 2, string)


@register.filter
def triplet_letters(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_numbers(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces_underscores(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces_underscores_spaces(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces_underscores_spaces_underscores(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces_underscores_spaces_underscores_spaces(string):
    """
    Given a string, return the string, tripleting every number character, and doubling every letter.
    All other characters should be output a single time each.
    """
    return re.sub(r'\d+', lambda m: m.group() * 3, string)


@register.filter
def triplet_letters_numbers_spaces_underscores_space