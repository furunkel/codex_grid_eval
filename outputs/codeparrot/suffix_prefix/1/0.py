def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string) - 1):
        prefixes.append(string[i:i + 1])
    return prefixes


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['a', 'ab', 'abc']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix('abc', 'abc')
    ['a', 'ab', 'abc']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_suffix(string: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_suffix('abc', 'abc')
    ['a', 'ab', 'abc']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes_with_prefix_and_suffix('abc', 'abc', 'abc')
    ['a', 'ab', 'abc']
    """
    suffixes = []
    for i in range(len(string) - 1):
        suffixes.append(string[i:i + 1])
    return suffixes


def all_suffixes_with_suffix_and_prefix(string: str, suffix: str, prefix: str) -> List[str]:
    """