def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('xyz')
    ['xyz', 'xy', 'x']
    """
    return [word for word in string.split() if len(word) > len(string)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('xyz')
    ['xyz', 'xy', 'x']
    """
    return [word for word in string.split() if len(word) > len(string)]


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('xyz', 'xy')
    ['xyz', 'xy', 'x']
    """
    return [word for word in string.split() if len(word) > len(prefix)]


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('xyz', 'xy')
    ['xyz', 'xy', 'x']
    """
    return [word for word in string.split() if len(word) > len(suffix)]


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('xyz', 'xy', 'x')
    ['xyz', 'xy', 'x']
    """
    return [word for word in string.split() if len(word) > len(prefix) and word.endswith(suffix)]


def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix_and_prefix('xyz', 'xy', 'x')
    ['xyz', 'xy', 'x']
    """
    return [word for word