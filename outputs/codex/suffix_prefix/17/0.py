
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('suffix')
    ['x', 'ix', 'fix', 'ffix', 'uffix', 'suffix']
    """
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('substring')
    ['s', 'u', 'b', 's', 't', 'r', 'i', 'n', 'g', 'su', 'ub', 'bs', 'st', 'tr', 'ri', 'in', 'ng', 'sub', 'ubs', 'bst', 'str', 'tri', 'rin', 'ing', 'subs', 'ubst', 'bstr', 'stri', 'trin', 'ring', 'subst', 'ubstr', 'bstri', 'strin', 'tring', 'substr', 'ubstri', 'bstrin', 'string', 'substri', 'ubstrin', 'bstring', 'substrin', 'ubstring', 'substring']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_substrings_2(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_2('substring')
    ['s', 'u', 'b', 's', 't', 'r', 'i', 'n', 'g', 'su', 'ub', 'bs', 'st', 'tr', 'ri', 'in', 'ng', 'sub', 'ubs', 'bst', 'str', 'tri', 'rin', 'ing', 'subs', 'ubst', 'bstr', 'stri', 'trin', 'ring', 'subst', 'ubstr', 'bstri', 'strin', 'tring', 'substr', 'ubstri', 'bstrin', 'string', 'substri', 'ubstrin', 'bstring', 'substrin', 'ubstring', 'substring']
    """
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def all_sub