
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every number.
    All other characters should be output a single time each.
    """
    return re.sub(r'([?])', lambda m: '?' * len(m.group()) * 2, string)


def remove_spaces(string):
    """
    Given a string, remove all spaces.
    """
    return re.sub(r'\s+', '', string)


def remove_newlines(string):
    """
    Given a string, remove all newlines.
    """
    return re.sub(r'\n', '', string)


def remove_newlines_and_spaces(string):
    """
    Given a string, remove all newlines and spaces.
    """
    return re.sub(r'\s+\n', ' ', string)


def remove_newlines_and_tabs(string):
    """
    Given a string, remove all newlines and tabs.
    """
    return re.sub(r'\n|\t', '', string)


def remove_newlines_and_tabs_and_spaces(string):
    """
    Given a string, remove all newlines and tabs and spaces.
    """
    return re.sub(r'\s+\n|\t|\s+', ' ', string)


def remove_newlines_and_tabs_and_spaces_and_quotes(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\'', '', string)


def remove_newlines_and_tabs_and_spaces_and_quotes_and_commas(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes and commas.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\,|\'', '', string)


def remove_newlines_and_tabs_and_spaces_and_quotes_and_commas_and_spaces(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes and commas.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\,|\ ', '', string)


def remove_newlines_and_tabs_and_spaces_and_quotes_and_commas_and_spaces_and_newlines(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes and commas.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\,|\ |\\n', '', string)


def remove_newlines_and_tabs_and_spaces_and_quotes_and_commas_and_spaces_and_newlines_and_tabs(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes and commas.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\,|\ |\\n|\\t', '', string)


def remove_newlines_and_tabs_and_spaces_and_quotes_and_commas_and_spaces_and_newlines_and_tabs_and_spaces(string):
    """
    Given a string, remove all newlines and tabs and spaces and quotes and commas.
    """
    return re.sub(r'\s+\n|\t|\s+|"|\,|\ |\\n|\\t|\ ', '', string)