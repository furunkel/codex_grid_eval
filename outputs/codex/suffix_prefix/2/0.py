
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('xyz')
    ['xyz', 'xy', 'x']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('xyz')
    ['xyz', 'yz', 'z']
    """
    return [string[i:] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('xyz')
    ['xyz', 'xy', 'x', 'yz', 'y', 'z']
    """
    return all_prefixes(string) + all_suffixes(string)


def all_substrings_of_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from longest to shortest of the input string
    >>> all_substrings_of_length('xyz', 2)
    ['xy', 'yz']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_of_length_with_overlap(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from longest to shortest of the input string
    >>> all_substrings_of_length_with_overlap('xyz', 2)
    ['xy', 'yz', 'yz', 'z']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)] + \
           [string[i:i + length] for i in range(len(string) - length + 2)]


def all_substrings_of_length_with_overlap_and_reverse(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from longest to shortest of the input string
    >>> all_substrings_of_length_with_overlap_and_reverse('xyz', 2