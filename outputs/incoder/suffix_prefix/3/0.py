
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('xyz')
    ['x', 'xy', 'xyz']
    """
    prefixes = []
    for c in string:
        prefixes.append(c)
        prefixes.extend(all_prefixes(c))
    return prefixes


@njit
def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('xyz')
    ['', 'y', 'z']
    """
    suffixes = []
    for c in string:
        suffixes.append(c)
        suffixes.extend(all_suffixes(c))
    return suffixes


@njit
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('xyz')
    ['', 'x', 'y', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings(c))
    return substrings


@njit
def all_substrings_without_repeats(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    without repeats
    >>> all_substrings_without_repeats('xyz')
    ['', 'x', 'y', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_without_repeats(c))
    return substrings


@njit
def all_substrings_with_prefixes(string: str) -> List[str]:
    """ Return list of all substrings with prefixes from shortest to longest of the input string
    >>> all_substrings_with_prefixes('xyz')
    ['', 'x', 'y', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_with_prefixes(c))
    return substrings


@njit
def all_substrings_with_suffixes(string: str) -> List[str]:
    """ Return list of all substrings with suffixes from shortest to longest of the input string
    >>> all_substrings_with_suffixes('xyz')
    ['', 'x', 'y', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_with_suffixes(c))
    return substrings


@njit
def all_substrings_without_prefixes(string: str) -> List[str]:
    """ Return list of all substrings without prefixes from shortest to longest of the input string
    >>> all_substrings_without_prefixes('xyz')
    ['', 'x', 'y', 'z']
    """
    substrings = []
    for c in string:
        substrings.append(c)
        substrings.extend(all_substrings_without_prefixes(c))
    return substrings


@njit
def all_substrings_without_suffixes(string: str) -> List[str]:
    """ Return 