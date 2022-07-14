def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    prefixes = []
    for i in range(len(string) - 1):
        prefixes.append(string[i:i + 2])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('12345678')
    ['12345678', '1234567', '123456', '12345', '1234', '123', '12', '1']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix('12345678', prefix='12345678')
    ['12345678', '12345678', '1234567', '12345', '1234', '123', '12', '1']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_suffix('12345678', suffix='12345678')
    ['12345678', '12345678', '1234567', '12345', '1234', '123', '12', '1']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 2])
    return suffixes


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes_with_prefix_and_suffix('12345678', prefix='12345678', suffix='12345678')
    ['12345678', '12345678', '1234567', '12345', '1234