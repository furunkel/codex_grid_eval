
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['x', 'ix', 'fix', 'ffix', 'uffix', 'suffix']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffixes('suffix')
    ['x', 'ix', 'fix', 'ffix', 'suffix', 'suffix']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffixes_from_string(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffixes_from_string('suffix')
    ['x', 'ix', 'fix', 'ffix', 'suffix', 'suffix']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffixes_from_list(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_suffixes_from_list('suffix')
    ['x', 'ix', 'fix', 'ffix', 'suffix', 'suffix']
    """
#    if not string:
#        return []
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes

def get_suffixes_from_file(file: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input file
    >>> get_suffixes_from_file('suffix')
    ['x', 'ix', 'fix', 'ffix', 'suffix', '