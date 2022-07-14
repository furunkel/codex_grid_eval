def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('prefix')
    ['prefix', 'prefi', 'pref', 'pre', 'pr', 'p']
    """
    prefixes = []
    for i in range(len(string) - 1):
        prefixes.append(string[i:i + 1])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'pre', 'pr', 'p']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('suffix', 'prefix')
    ['suffix', 'pre', 'pr', 'p']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('suffix', 'suffix')
    ['suffix', 'pre', 'pr', 'p']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('suffix', 'prefix', 'suffix')
    ['suffix', 'pre', 'pr', 'p']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_suffix_and