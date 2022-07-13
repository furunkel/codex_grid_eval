
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    suffixes = []
    for suffix in suffixes_iter(string):
        suffixes.append(suffix)
    return suffixes


def suffixes_iter(string: str) -> Iterator[str]:
    """ Return iterator of suffixes from longest to shortest of the input string
    >>> list(suffixes_iter('suffix'))
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    length = len(string)
    if length == 0:
        yield ''
        return
    if length == 1:
        yield string
        return
    suffixes = [string[length - i] for i in range(1, length)]
    for suffix in suffixes:
        yield suffix


def prefixes_iter(string: str) -> Iterator[str]:
    """ Return iterator of prefixes from longest to shortest of the input string
    >>> list(prefixes_iter('suffix'))
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    length = len(string)
    if length == 0:
        yield ''
        return
    if length == 1:
        yield string
        return
    prefixes = [string[: length - i] for i in range(1, length)]
    for prefix in prefixes:
        yield prefix


def common_prefix(strings: List[str]) -> str:
    """ Return common prefix of all input strings
    >>> common_prefix(['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x'])
    'fix'
    """
    common_prefix_length = 0
    for string in strings:
        common_prefix_length = min(len(string), common_prefix_length)
    return strings[common_prefix_length]


def common_suffix(strings: List[str]) -> str:
    """ Return common suffix of all input strings
    >>> common_suffix(['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x'])
    'ix'
    """
    common_suffix_length = 0
    for string in strings:
        common_suffix_length = min(len(string), common_suffix_length)
    return strings[-common_suffix_length]


def common_prefix_suffix(strings: List[str]) -> str:
    """ Return common prefix and suffix of all input strings
    >>> common_prefix_suffix(['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x'])
    ('fix', 'ix')
    """
    common_prefix_length = 0
    common_suffix_length = 0
    for string in strings:
        common_prefix_length = min(len(string), common_prefix_length)
        common_suffix_length = min(len(string), common_suffix_length)
    return strings[common_prefix_length], strings[-common_suffix_length]


def common_prefix_suffixes(strings: List[str]) -> List[Tuple[str, str]]:
    """ Return common prefix and suffix of all input strings
    >>> common_prefix_suffixes(['suffix', 'uffix', 'ffix', 'fix', '