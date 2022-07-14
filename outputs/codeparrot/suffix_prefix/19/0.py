def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('prefix')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    prefixes = []
    for prefix in string.split():
        prefixes.append(prefix)
        if len(prefixes) > 1:
            break
    return prefixes


def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes('prefix')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    suffixes = []
    for suffix in string.split():
        suffixes.append(suffix)
        if len(suffixes) > 1:
            break
    return suffixes


def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_prefix('prefix', 'x')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    suffixes = []
    for suffix in string.split():
        suffixes.append(suffix)
        if len(suffixes) > 1:
            break
    return suffixes


def get_all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_suffix('prefix', 'x')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    suffixes = []
    for suffix in string.split():
        suffixes.append(suffix)
        if len(suffixes) > 1:
            break
    return suffixes


def get_all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_prefix_and_suffix('prefix', 'x', 'ix')
    ['x', 'ix', 'fix', 'efix', 'refix', '