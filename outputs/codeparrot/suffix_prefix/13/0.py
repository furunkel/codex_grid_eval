def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [s for s in string.split() if len(s) > len(string.split())]


def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [s for s in string.split() if len(s) > len(string.split())]


def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_prefix('abc', 'abc')
    ['c', 'bc', 'abc']
    """
    return [s for s in string.split() if len(s) > len(prefix.split())]


def get_all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_suffix('abc', 'abc')
    ['c', 'bc', 'abc']
    """
    return [s for s in string.split() if len(s) > len(suffix.split())]


def get_all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes_with_prefix_and_suffix('abc', 'abc', 'abc')
    ['c', 'bc', 'abc']
    """
    return [s for s in string.split() if len(s) > len(prefix.split()) and len(s) > len(suffix.split())]


def get_all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> get_all_suffixes