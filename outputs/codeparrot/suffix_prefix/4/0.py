def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    prefixes = []
    for i in range(len(string) - 1):
        prefixes.append(string[i:i + 2])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('suffix', 'suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('suffix', 'suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('suffix', 'suffix', 'suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    suffixes