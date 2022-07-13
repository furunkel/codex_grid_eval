
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return list(itertools.takewhile(lambda s: len(s) <= len(string), itertools.accumulate(string.split(), lambda s, x: s + x)))


def all_suffixes_count(string: str) -> int:
    """ Return count of all suffixes from shortest to longest of the input string
    >>> all_suffixes_count('abc')
    3
    """
    return len(all_suffixes(string))


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: len(s) > len(string), itertools.accumulate(string.split(), lambda s, x: s + x)))


def all_prefixes_count(string: str) -> int:
    """ Return count of all prefixes from shortest to longest of the input string
    >>> all_prefixes_count('abc')
    3
    """
    return len(all_prefixes(string))


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['', 'a', 'ab', 'abc']
    """
    return list(itertools.takewhile(lambda s: len(s) <= len(string), itertools.accumulate(string.split(), lambda s, x: s + x)))


def all_substrings_count(string: str) -> int:
    """ Return count of all substrings from shortest to longest of the input string
    >>> all_substrings_count('abc')
    3
    """
    return len(all_substrings(string))


def all_substrings_count_with_prefix(string: str) -> int:
    """ Return count of all substrings with prefix from shortest to longest of the input string
    >>> all_substrings_count_with_prefix('abc')
    3
    """
    return len(all_substrings(string))


def all_substrings_count_with_prefix_and_suffix(string: str) -> int:
    """ Return count of all substrings with prefix and suffix from shortest to longest of the input string
    >>> all_substrings_count_with_prefix_and_suffix('abc')
    3
    """
    return len(all_substrings(string))


def all_substrings_count_with_prefix_and_suffix_and_prefix(string: str) -> int:
    """ Return count of all substrings with prefix and suffix with prefix from shortest to longest of the input string
    >>> all_substrings_count_with_prefix_and_suffix_and_prefix('abc')
    3
    """
    return len(all_substrings(string))


def all_substrings_count_with_prefix_and_suffix_and_prefix_and_suffix(string: str) -> int:
    """ Return count of all substrings with prefix and suffix with prefix and suffix from shortest to longest of the input string
    >>> all_substrings_