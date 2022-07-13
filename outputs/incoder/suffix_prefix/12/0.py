
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@lru_cache(maxsize=1024)
def all_prefixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.startswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.startswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.startswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings_prefixes_suffixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes_suffixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings_prefixes_suffixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_prefixes_suffixes_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@lru_cache(maxsize=1024)
def all_substrings_suffixes_prefixes_prefixes(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_suffixes_prefixes_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: not s.endswith(string), string))


@lru_cache(maxsize=1024)
def 