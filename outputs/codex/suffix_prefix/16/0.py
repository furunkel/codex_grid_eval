
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    return [string[i:] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('prefix')
    ['prefix', 'refix', 'efix', 'fix', 'ix', 'x']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings of the input string
    >>> all_substrings('substring')
    ['substring', 'ubstring', 'bstring', 'string', 'tring', 'ring', 'ing', 'ng', 'g']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length
    >>> all_substrings_with_length('substring', 3)
    ['sub', 'ubs', 'bst', 'str', 'tri', 'rin', 'ing']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length and offset
    >>> all_substrings_with_length_and_offset('substring', 3, 2)
    ['ubstring', 'bstring', 'string', 'tring', 'ring', 'ing']
    """
    return [string[i:i + length] for i in range(offset, len(string) - length + 1)]


def all_substrings_with_length_and_offset_and_step(string: str, length: int, offset: int, step: int) -> List[str]:
    """ Return list of all sub