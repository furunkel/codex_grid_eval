def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    return [
        s[len(string):]
        for s in re.findall(r'\w+', string)
        if len(s) > len(string)
    ]


def get_all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    return [
        s[len(string):]
        for s in re.findall(r'\w+', string)
        if len(s) > len(string)
    ]


def get_all_suffixes_with_prefix(string: str, prefix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_prefix('prefix', 'prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    return [
        s[len(prefix):]
        for s in re.findall(r'\w+', string)
        if len(s) > len(prefix)
    ]


def get_all_suffixes_with_prefix_and_suffix(string: str, prefix: str, suffix: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> get_all_suffixes_with_prefix_and_suffix('prefix', 'prefix', 'suffix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    return [
        s[len(prefix):]
        for s in re.findall(r'\w+', string)
        if len(s) > len(prefix) and len(s) > len(suffix)
    ]


def get_all_suffixes_with_prefix_and_suffix_and_prefix(string: str, prefix: str, suffix: str, prefix_and_suffix: str) -> List[str]:
    """ Return list of