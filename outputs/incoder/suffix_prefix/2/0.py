
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('xyz')
    ['xyz', 'xy', 'x']
    """
    prefixes = []
    for c in string:
        prefixes.append(c)
        prefixes.extend(all_prefixes(c))
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    suffixes = []
    for c in reversed(string):
        suffixes.append(c)
        suffixes.extend(all_suffixes(c))
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('xyz')
    ['xyz', 'yz', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings(c))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes('xyz')
    ['xyz', 'yz', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_prefixes(c))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    substrings = []
    for c in reversed(string):
        substrings.append(c)
        substrings.extend(all_substrings_suffixes(c))
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_prefixes_suffixes(c))
    return substrings


def all_substrings_prefix_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefix_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_prefix_suffixes(c))
    return substrings


def all_substrings_prefix_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefix_suffixes_prefixes