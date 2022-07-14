def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!', 'reverse the result!', 'reverse the result', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the r', 'reverse the ', 'reverse the', 'reverse th', 'reverse t', 'reverse ', 'reverse', 'revers', 'rever', 'reve', 'rev', 're', 'r']
    """
    prefixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            prefixes.append(string[i + 1:])
        else:
            prefixes.append(string[i])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!', 'reverse the result!!!', 'reverse the result', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the ', 'reverse th', 'reverse t', 'reverse ', 'reverse ', 'reverse ', 'revers', 'rever', 'reve', 'rev', 're', 'r']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == ' ':
            suffixes.append(string[i + 1:])
        else:
            suffixes.append(string[i])
    return suffixes


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!!', 'reverse the result!!!', 'reverse the result!!!', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the ', 'reverse th', 'reverse t', 'reverse ', 'reverse ', 'reverse ', 'revers', 'rever', 'reve', 'rev', 're', 'r']
   