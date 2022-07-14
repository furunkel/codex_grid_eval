def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(v) for v in values if v is not None]


def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3]
    """
    return [int(v) for v in values if v is not None]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(v) for v in values if v is not None]


def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6]
    """
    return [list(v) for v in values if v is not None]


def filter_dicts(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    {'abc': 'abc'}
    """
    return [dict(v) for v in values if v is not None]


def filter_nones(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for Nones
    >>> filter_nones([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6]
    """
    return [None] * len(values)


def filter_nones_and_nones(values: List[Any], nones