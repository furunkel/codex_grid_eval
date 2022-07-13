
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('prefix')
    ['prefix', 'prefi', 'pref', 'pre', 'pr', 'p']
    """
    return [string[:i] for i in range(len(string), 0, -1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('suffix')
    ['suffix', 'uffix', 'ffix', 'fix', 'ix', 'x']
    """
    return [string[i:] for i in range(len(string), 0, -1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from longest to shortest of the input string
    >>> all_substrings('substring')
    ['substring', 'ubstring', 'bstring', 'string', 'tring', 'ring', 'ing', 'ng', 'g', 'ubstrin', 'bstrin', 'strin', 'trin', 'rin', 'in', 'n', 'ubstri', 'bstri', 'stri', 'tri', 'ri', 'i', 'ubstr', 'bstr', 'str', 'tr', 'r', 'ubst', 'bst', 'st', 't', 'ubs', 'bs', 's', 'ub', 'b', 'u', 'substrin', 'ubstrin', 'bstrin', 'strin', 'trin', 'rin', 'in', 'n', 'substri', 'ubstri', 'bstri', 'stri', 'tri', 'ri', 'i', 'substr', 'ubstr', 'bstr', 'str', 'tr', 'r', 'subst', 'ubst', 'bst', 'st', 't', 'subs', 'ubs', 'bs', 's', 'sub', 'ubs', 'ub', 'b', 'su', 'u', 's']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_with_length(string: str, length: int) -> List[str]:
    """ Return list of all substrings of length from longest to shortest of the input string
    >>> all_substrings_with