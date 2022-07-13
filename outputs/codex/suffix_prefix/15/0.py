
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('xyz')
    ['z', 'yz', 'xyz']
    """
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('xyz')
    ['x', 'y', 'z', 'xy', 'yz', 'xyz']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_of_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from shortest to longest of the input string
    >>> all_substrings_of_length('xyz', 2)
    ['xy', 'yz']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_of_length_with_overlap(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from shortest to longest of the input string
    >>> all_substrings_of_length_with_overlap('xyz', 2)
    ['xy', 'yz', 'yz', 'xyz']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1) for j in range(length)]


def all_substrings_of_length_with_overlap_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of length from shortest to longest of the input string
    >>> all_substrings_of_length_with_overlap_and_offset('xyz', 2, 1)
    ['xy', 'yz', 'yz', 'xyz']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1) for j in range(length) if i + j >= offset]


def all_substrings_of_length_with_overlap_and_offset_and_max_length(