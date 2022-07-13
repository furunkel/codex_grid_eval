
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length
    >>> all_substrings_with_length('abc', 2)
    ['ab', 'bc']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length and offset
    >>> all_substrings_with_length_and_offset('abc', 2, 1)
    ['bc']
    """
    return [string[i:i + length] for i in range(offset, len(string) - length + 1)]


def all_substrings_with_length_and_offset_and_step(string: str, length: int, offset: int, step: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length, offset and step
    >>> all_substrings_with_length_and_offset_and_step('abc', 2, 1, 2)
    ['bc']
    """
    return [string[i:i + length] for i in range(offset, len(string) - length + 1, step)]


def all_substrings_with_length_and_step(string: str, length: int, step: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length and step
    >>> all_substrings