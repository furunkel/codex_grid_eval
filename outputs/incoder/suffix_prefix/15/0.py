
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('xyz')
    ['z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('xyz')
    ['x', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_substrings('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_substrings_prefixes('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_substrings_suffixes('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substrings_substrings_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_substrings_substrings('xyz')
    ['x', 'y', 'z', 'yz', 'xyz']
    """
    return list(itertools.accumulate(string.split(), lambda x, y: x + y))


def all_substring