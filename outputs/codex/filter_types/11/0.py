
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
    return [value for value in values if isinstance(value, dict)]


def filter_lists(values: List[Any]) -> List[List]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
    """
    return [value for value in values if isinstance(value, list)]


def filter_sets(values: List[Any]) -> List[Set]:
    """ Filter given list of any python values only for sets
    >>> filter_sets([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [set()]
    """
    return [value for value in values if isinstance(value, set)]


def filter_frozensets(values: List[Any]) -> List[FrozenSet]:
    """ Filter given list of any python values only for frozensets
    >>> filter_frozensets([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [frozenset()]
    """
    return [value for value in values if isinstance(value, frozenset)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [value for value in values if isinstance(value, str)]


def filter_bytes(values: List[Any]) -> List[bytes]:
    """ Filter given list of any python values only for bytes
    >>> filter_bytes([1, 2, 3, 3.6, 'abc', {}, [