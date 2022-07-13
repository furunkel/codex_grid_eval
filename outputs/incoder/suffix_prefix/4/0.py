
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('suffix')
    ['suffix', 'suffi', 'suff', 'suf', 'su', 's']
    """
    prefixes = []
    for s in string:
        prefixes.append(s)
        prefixes.extend(all_prefixes(s))
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    suffixes = []
    for s in string:
        suffixes.append(s)
        suffixes.extend(all_suffixes(s))
    return suffixes


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings(s))
    return substrings


def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_prefixes(s))
    return substrings


def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_suffixes('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_suffixes(s))
    return substrings


def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_prefixes_suffixes(s))
    return substrings


def all_substrings_prefixes_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes_prefixes('suffix')
    ['suffix', 'suff', 'suf', 'su', 's']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_prefixes_suffixes_prefixes(s))
    return substrings


def all_substrings_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from 