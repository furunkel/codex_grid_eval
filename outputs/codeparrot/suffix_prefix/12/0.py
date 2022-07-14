def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    """
    return [s for s in string.split() if len(s) > len(string.split())]


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('abc', 'bc')
    ['abc', 'bc']
    """
    return [s for s in string.split() if len(s) > len(prefix.split())]


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('abc', 'bc')
    ['abc', 'bc']
    """
    return [s for s in string.split() if len(s) > len(suffix.split())]


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('abc', 'bc')
    ['abc', 'bc']
    """
    return [s for s in string.split() if len(s) > len(prefix.split()) and len(s) > len(suffix.split())]


def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix_and_prefix('abc', 'bc')
    ['abc', 'bc']
    """
    return [s for s in string.split() if len(s) > len(suffix.split()) and len(s) > len(prefix.split())]


def all_suffixes_with_suffix_and_prefix_and_suffix(string: str, suffix: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from