
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('prefix')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    suffixes = []
    prefix = string
    while len(prefix) > 0:
        suffixes.append(prefix[-1])
        prefix = prefix[:-1]
    return suffixes


@njit
def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('suffix')
    ['s', 'ix', 'fix', 'efix', 'refix', 'suffix']
    """
    prefixes = []
    suffix = string
    while len(suffix) > 0:
        prefixes.append(suffix[0])
        suffix = suffix[1:]
    return prefixes


@njit
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('prefix')
    ['prefix', 'pre', 'prex', 'prefixx', 'prefixix', 'prefixfix', 'prefixefix', 'prefixrefix', 'prefixprefix']
    """
    substrings = []
    prefix = string
    while len(prefix) > 0:
        substrings.append(prefix)
        prefix = prefix[:-1]
    return substrings


@njit
def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes('prefix')
    ['prefix', 'pre', 'prex', 'prefixx', 'prefixix', 'prefixfix', 'prefixefix', 'prefixrefix', 'prefixprefix']
    """
    substrings = []
    prefix = string
    while len(prefix) > 0:
        substrings.append(prefix[0])
        prefix = prefix[1:]
    return substrings


@njit
def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes('suffix')
    ['suffix', 'su', 'sux', 'suffixx', 'suffixix', 'suffixfix', 'suffixefix', 'suffixrefix', 'suffixsuffix']
    """
    substrings = []
    suffix = string
    while len(suffix) > 0:
        substrings.append(suffix[-1])
        suffix = suffix[:-1]
    return substrings


@njit
def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes_suffixes('suffix')
    ['suffix', 'su', 'sux', 'suffixx', 'suffixix', 'suffixfix', 'suffixefix', 'suffixrefix', 'suffixsuffix']
    """
    substrings = []
    prefix = string
    while len(prefix) > 0:
        substrings.append(prefix[0])
        prefix = prefix[1:]
        suffix = string
        while len(suffix) > 0:
            substrings.append(suffix[-1])
            suffix = suffix[:-1]
    return 