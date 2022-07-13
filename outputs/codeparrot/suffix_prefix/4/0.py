
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
#    print(string)
    prefixes = []
    for i in range(len(string)):
        if string[i] in prefixes:
            prefixes.remove(string[i])
    return prefixes

def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.remove(string[i])
    return suffixes

def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('suffix', 'suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.remove(string[i])
    return suffixes

def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('suffix', 'suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.remove(string[i])
    return suffixes

def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_