
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    """
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_of_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string of the given length
    >>> all_substrings_of_length('abc', 2)
    ['ab', 'bc']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_of_length_at_least(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string of length at least the given length
    >>> all_substrings_of_length_at_least('abc', 2)
    ['ab', 'abc', 'bc']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + length, len(string) + 1)]


def all_substrings_of_length_at_most(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string of length at most the given length
    >>> all_substrings_of_length_at_most('abc', 2)
    ['a', 'ab', 'b', 'bc', 'c']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, min(i + length + 1, len(string) + 1))]


def all_substrings_of_length_between(string: str, min_length: int, max_length: int) -> List[str]:
    """ Return list of all substrings of the input string