
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    suffixes = []
    length = len(string)
    for index in range(length):
        suffixes.append(string[index:])
    return suffixes


@njit
def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    prefixes = []
    length = len(string)
    for index in range(length - 1, -1, -1):
        prefixes.append(string[:index])
    return prefixes


@njit
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length):
        substrings.append(string[index:index+1])
    return substrings


@njit
def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length - 1, -1, -1):
        substrings.append(string[index:index+1])
    return substrings


@njit
def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length - 1, -1, -1):
        substrings.append(string[index:index+1])
    return substrings


@njit
def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_prefixes_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
    substrings = []
    length = len(string)
    for index in range(length - 1, -1, -1):
        substrings.append(string[index:index+1])
    return substrings


@njit
def all_substrings_prefixes_suffixes_prefix