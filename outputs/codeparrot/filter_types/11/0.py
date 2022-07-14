def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """
    return [tuple(value) for value in values if value is not None]


def filter_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([{'a': 1}, {'b': 2}, {'c': 3}])
    [{'a': 1}, {'b': 2}, {'c': 3}]
    """
    return [dict(value) for value in values if value is not None]


def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {'a': 1}, {'b': 2}, {'c': 3}]
    """
    return [list(value) for value in values if value is not None]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    []
    """
    return [value for value in values if value is not None]


def filter_none_or_str(values: List[Any], default: str) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none_or_str([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {'a': 1}, {'b': 2}, {'c': 3}]
    """
    return [value for value in values if value is not None and value is not str(default)]


def filter_none_or_list(values: List[Any], default: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none_or_list([