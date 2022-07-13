
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    prefixes = []
    for s in string:
        prefixes.append(s)
        prefixes.extend(all_prefixes(s))
    return prefixes


@lru_cache(maxsize=1024)
def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['8', '7', '6', '5', '4', '3', '2', '1']
    """
    suffixes = []
    for s in string:
        suffixes.append(s)
        suffixes.extend(all_suffixes(s))
    return suffixes


@lru_cache(maxsize=1024)
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings(s))
    return substrings


@lru_cache(maxsize=1024)
def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_prefixes(s))
    return substrings


@lru_cache(maxsize=1024)
def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_suffixes('12345678')
    ['8', '7', '6', '5', '4', '3', '2', '1']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_suffixes(s))
    return substrings


@lru_cache(maxsize=1024)
def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    substrings = []
    for s in string:
        substrings.append(s)
        substrings.extend(all_substrings_prefixes_suffixes(s))
    return substrings


@lru_cache(maxsize=1024)
def all_substrings_prefixes_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_