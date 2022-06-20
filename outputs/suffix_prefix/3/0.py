
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('xyz')
    ['x', 'xy', 'xyz']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
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


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length
    >>> all_substrings_with_length('xyz', 2)
    ['xy', 'yz']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length and offset
    >>> all_substrings_with_length_and_offset('xyz', 2, 1)
    ['yz']
    """
    return [string[i:i + length] for i in range(offset, len(string) - length + 1)]


def all_substrings_with_length_and_offset_and_step(string: str, length: int, offset: int, step: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length, offset and step
    >>> all_substrings_with_length_and_offset_and_step('xyz', 2, 1, 2)
    ['yz']
   