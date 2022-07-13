
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('suffix')
    ['s', 'su', 'suf', 'suff', 'suffi', 'suffix']
    """
    prefixes = []
    for c in string:
        if c in string.ascii_lowercase:
            prefixes.append(c)
        else:
            prefixes.extend(all_prefixes(c))
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['f', 'ffi', 'ffif', 'ffiffiffi', 'ffiffiffif', 'ffiffiffiffi', 'ffiffiffif', 'ffiffiffiffiffi']
    """
    suffixes = []
    for c in string:
        if c in string.ascii_lowercase:
            suffixes.append(c)
        else:
            suffixes.extend(all_suffixes(c))
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('suffix')
    ['f', 'ffi', 'ffif', 'ffiffi', 'ffiffif', 'ffiffiffi', 'ffiffiffi', 'ffiffiffif', 'ffiffiffiffiffi']
    """
    substrings = []
    for c in string:
        if c in string.ascii_lowercase:
            substrings.append(c)
        else:
            substrings.extend(all_substrings(c))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string with prefixes
    >>> all_substrings_prefixes('suffix')
    ['f', 'ffi', 'ffif', 'ffiffi', 'ffiffif', 'ffiffiffi', 'ffiffiffi', 'ffiffiffif', 'ffiffiffiffiffi']
    """
    substrings = []
    for c in string:
        if c in string.ascii_lowercase:
            substrings.append(c)
        else:
            substrings.extend(all_substrings_prefixes(c))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string with suffixes
    >>> all_substrings_suffixes('suffix')
    ['f', 'ffi', 'ffif', 'ffiffi', 'ffiffif', 'ffiffiffi', 'ffiffiffi', 'ffiffiffif', 'ffiffiffiffiffi']
    """
    substrings = []
    for c in string:
        if c in string.ascii_lowercase:
            substrings.append(c)
        else:
            substrings.extend(all_substrings_suffixes(c))
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string with prefixes and suffixes
    >>> all_substrings_prefixes_suffixes('suffix')
    ['f', 'ffi', 'ffif', 'ffiffi', 'ffif', 'ffiffi