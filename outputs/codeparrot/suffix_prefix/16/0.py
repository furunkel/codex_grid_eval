
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_suffix_list('suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list_all(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_suffix_list_all('suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list_all_all(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_suffix_list_all_all('suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffix_list_all_all_all(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_suffix_list_all_all_all('suffix')
    ['