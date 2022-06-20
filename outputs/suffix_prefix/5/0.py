
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('suffix')
    ['s', 'su', 'suf', 'suff', 'suffi', 'suffix']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('prefix')
    ['x', 'ix', 'fix', 'efix', 'refix', 'prefix']
    """
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('substring')
    ['s', 'su', 'sub', 'subs', 'subst', 'substr', 'substri', 'substrin', 'substring', 'u', 'ub', 'ubs', 'ubst', 'ubstr', 'ubstri', 'ubstrin', 'ubstring', 'b', 'bs', 'bst', 'bstr', 'bstri', 'bstrin', 'bstring', 's', 'st', 'str', 'stri', 'strin', 'string', 't', 'tr', 'tri', 'trin', 'tring', 'r', 'ri', 'rin', 'ring', 'i', 'in', 'ing', 'n', 'ng', 'g']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of the input string with the given length
    >>> all_substrings_with_length('substring', 3)
    ['sub', 'ubs', 'bst', 'str', 'tri', 'rin', 'ing']
    """
    return [string[i:i + length] for i in range(len(string) - length + 1)]


def all_substrings_with_length_and_offset(string: str, length: int, offset: int) -> List[str]:
    """ Return list of all substrings of the input string