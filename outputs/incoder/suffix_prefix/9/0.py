
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """
    prefixes = []
    current = []
    for c in string:
        if c.isalpha():
            current.append(c)
        else:
            prefixes.append(''.join(current))
            current = []
    prefixes.append(''.join(current))
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['!', '!!', '!!!']
    """
    suffixes = []
    current = []
    for c in string:
        if c.isalpha():
            current.append(c)
        else:
            suffixes.append(''.join(current))
            current = []
    suffixes.append(''.join(current))
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """
    substrings = []
    current = []
    for c in string:
        if c.isalpha():
            current.append(c)
        else:
            substrings.append(''.join(current))
            current = []
    substrings.append(''.join(current))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string with prefixes
    >>> all_substrings_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """
    substrings = []
    current = []
    for c in string:
        if c.isalpha():
            current.append(c)
        else:
            substrings.append(''.join(current))
            current = []
    substrings.append(''.join(current))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string with suffixes
    >>> all_substrings_suffixes('reverse the result!!!')
    ['!', '!!', '!!!']
    """
    substrings = []
