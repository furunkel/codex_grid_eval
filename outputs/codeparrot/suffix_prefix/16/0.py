def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == 'x':
            suffixes.append(string[i + 1])
        else:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes('suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == 'x':
            suffixes.append(string[i + 1])
        else:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_prefix('suffix', 'suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == prefix:
            suffixes.append(string[i + 1])
        else:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_suffix_prefix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_suffix_prefix('suffix', 'suffix')
    ['suffix', 'suffix', 'ffix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for i in range(len(string) - 1):
        if string[i] == suffix:
            suffixes.append(string[i + 1])
        else:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_prefix_suffix