def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resu', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!', 'reverse the result!!!']
    """
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            prefixes.append(string[i + 1:])
        else:
            prefixes.append(string[i])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!!']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            suffixes.append(string[i + 1:])
        else:
            suffixes.append(string[i])
    return suffixes


def all_suffixes_reverse(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_reverse('reverse the result!!!')
    ['r', 're', 'rev', 'reve', 'rever', 'revers', 'reverse', 'reverse ', 'reverse t', 'reverse th', 'reverse the', 'reverse the ', 'reverse the r', 'reverse the re', 'reverse the res', 'reverse the resul', 'reverse the result', 'reverse the result!', 'reverse the result!!!']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i