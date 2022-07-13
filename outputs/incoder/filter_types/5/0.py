
def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [float(v) for v in values if isinstance(v, float)]


def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_ints([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [int(v) for v in values if isinstance(v, int)]


def filter_strs(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strs([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(v) for v in values if isinstance(v, str)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [v for v in values if v is not None]


def filter_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for empty strings
    >>> filter_empty([None, 1, 2, 3, 3.6, '', {}, [], (1,)])
    [None, 1, 2, 3]
    """
    return [v for v in values if v != ""]


def filter_not_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for non-empty strings
    >>> filter_not_empty([None, 1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [v for v in values if v != ""]


def filter_contains(values: List[Any], substring: str) -> List[Any]:
    """ Filter given list of any python values only for strings containing substring
    >>> filter_contains(['abc', 'def', 'ghi'], 'abc')
    ['abc']
    """
    return [v for v in values if substring in v]


def filter_not_contains(values: List[Any], substring: str) -> List[Any]:
    """ Filter given list of any python values only for strings NOT containing substring
    >>> filter_not_contains(['abc', 'def', 'ghi'], 'abc')
    ['def', 'ghi']
    """
    return [v for v in values if substring not in v]


def filter_greater_than(values: List[Any], threshold: int) -> List[Any]:
    """ Filter given list of any python values only for values above threshold
    >>> filter_greater_than([10, 20, 30, 40], 30)
    [40]
    """
    return [v for v in values if v > threshold]


def filter_greater_than_or_equal(values: List[Any], threshold: int) -> List[Any]:
    """ Filter given list of any python values only for values above or equal to threshold
    >>> filter_greater_than_or_equal([10, 20, 30, 40], 30)
    [10, 20, 30]
    """
