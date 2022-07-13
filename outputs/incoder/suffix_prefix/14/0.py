
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@curry
def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_prefixes('xyz')
    ['xyz', 'yz', 'z']
    """
    return list(itertools.takewhile(lambda s: not s.startswith(string), string))


@curry
def all_substrings(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring in s, string))


@curry
def all_substrings_without_repeating(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_repeating('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring not in s, string))


@curry
def all_substrings_without_repeating_suffixes(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_repeating_suffixes('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring not in all_suffixes(s), string))


@curry
def all_substrings_without_repeating_prefixes(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_repeating_prefixes('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring not in all_prefixes(s), string))


@curry
def all_substrings_without_repeating_substrings(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_repeating_substrings('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring not in all_substrings(s, substring), string))


@curry
def all_substrings_without_repeating_substrings_suffixes(string: str, substring: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings_without_repeating_substrings_suffixes('xyz', 'xyz')
    ['xyz']
    """
    return list(itertools.takewhile(lambda s: substring not in all_substrings_without_repeating_suffixes(s, substring), string))


@curry
def all_substrings_without_repeating_substring