
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    """
    return [value for value in values if isinstance(value, int)]


def filter_integers_v2(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v2(['a', 3.14, 5])
    [5]
    """
    return list(filter(lambda x: isinstance(x, int), values))


def filter_integers_v3(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v3(['a', 3.14, 5])
    [5]
    """
    return list(filter(isinstance, values, [int] * len(values)))


def filter_integers_v4(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v4(['a', 3.14, 5])
    [5]
    """
    return list(filter(isinstance, values, [int] * len(values)))


def filter_integers_v5(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v5(['a', 3.14, 5])
    [5]
    """
    return list(filter(isinstance, values, [int] * len(values)))


def filter_integers_v6(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v6(['a', 3.14, 5])
    [5]
    """
    return list(filter(isinstance, values, [int] * len(values)))


def filter_integers_v7(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers_v7(['a', 3.14, 5])
    [5]
    """
    return list(filter(isinstance, values, [int] * len(