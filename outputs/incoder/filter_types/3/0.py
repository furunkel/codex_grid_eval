
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1.0, 2.0, 3.0]
    """
    return [x for x in values if isinstance(x, float)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['1', '2', '3', '3.6', 'abc', '{}', '[]', '1']
    """
    return [x for x in values if isinstance(x, str)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for none
    >>> filter_none([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x is None]


def filter_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for empty
    >>> filter_empty([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if not x]


def filter_nonempty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for nonempty
    >>> filter_nonempty([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x]


def filter_emptystring(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for emptystring
    >>> filter_emptystring([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x != ""]


def filter_nonemptystring(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for nonemptystring
    >>> filter_nonemptystring([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x]


def filter_emptylist(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for emptylist
    >>> filter_emptylist([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x != []]


def filter_nonemptylist(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for nonemptylist
    >>> filter_nonemptylist([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [x for x in values if x]