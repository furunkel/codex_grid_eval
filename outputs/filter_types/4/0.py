
def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    """
    return [value for value in values if isinstance(value, float)]


def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints(['a', 3.14, 5])
    [5]
    """
    return [value for value in values if isinstance(value, int)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [value for value in values if isinstance(value, str)]


def filter_lists(values: List[Any]) -> List[List]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, [1, 2, 3]])
    [[1, 2, 3]]
    """
    return [value for value in values if isinstance(value, list)]


def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, (1, 2, 3)])
    [(1, 2, 3)]
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts(['a', 3.14, {'a': 1, 'b': 2}])
    [{'a': 1, 'b': 2}]
    """
    return [value for value in values if isinstance(value, dict)]


def filter_sets(values: List[Any]) -> List[Set]:
    """ Filter given list of any python values only for sets
    >>> filter_sets(['a', 3.14, {1, 2, 3}])
    [{1, 2, 3}]
    """
    return [value for value in values if isinstance(value, set)]


