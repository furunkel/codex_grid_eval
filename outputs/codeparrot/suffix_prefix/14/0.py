def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    return [x for x in string.split() if x.startswith(longest)]


def get_longest_prefix(string: str) -> str:
    """ Return longest prefix from longest to shortest of the input string
    >>> get_longest_prefix('xyz')
    'xyz'
    """
    return longest_prefix(string)


def get_longest_suffix(string: str) -> str:
    """ Return longest suffix from longest to shortest of the input string
    >>> get_longest_suffix('xyz')
    'xyz'
    """
    return longest_suffix(string)


def get_longest_prefix_length(string: str) -> int:
    """ Return longest prefix length from longest to shortest of the input string
    >>> get_longest_prefix_length('xyz')
    2
    """
    return len(longest_prefix(string))


def get_longest_suffix_length(string: str) -> int:
    """ Return longest suffix length from longest to shortest of the input string
    >>> get_longest_suffix_length('xyz')
    2
    """
    return len(longest_suffix(string))


def get_longest_prefix_length_length(string: str) -> int:
    """ Return longest prefix length from longest to shortest of the input string
    >>> get_longest_prefix_length_length('xyz')
    2
    """
    return len(longest_prefix_length(string))


def get_longest_suffix_length_length(string: str) -> int:
    """ Return longest suffix length from longest to shortest of the input string
    >>> get_longest_suffix_length_length('xyz')
    2
    """
    return len(longest_suffix_length(string))


def get_longest_prefix_length_length(string: str) -> int:
    """ Return longest prefix length from longest to shortest of the input string
    >>> get_longest_prefix_length_length('xyz')
    2
    """
    return len(longest_prefix_length(string))


def get_longest_suffix_length_length(string: str) -> int:
    """ Return longest suffix length from longest to shortest of