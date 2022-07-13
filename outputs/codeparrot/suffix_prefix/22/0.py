
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes('12345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_prefix('12345678', '2345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_suffix('12345678', '2345678')
    ['12345678', '2345678', '345678', '45678', '5678', '678', '78', '8']
    """
#    print(string)
    suffixes = []
    for i in range(len(string)):
        if string[i] in suffixes:
            suffixes.append(string[i])
    return suffixes


def get_all_suffixes_with_prefix_and_suffix(string: str, prefix: str,