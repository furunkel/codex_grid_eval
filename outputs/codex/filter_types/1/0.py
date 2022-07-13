
def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [value for value in values if isinstance(value, str)]


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """
    return [value for value in values if isinstance(value, float)]


def filter_lists(values: List[Any]) -> List[List]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
    """
    return [value for value in values if isinstance(value, list)]


def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_sets(values: List[Any]) -> List[Set]:
    """ Filter given list of any python values only for sets
    >>> filter_sets([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [set()]
    """
    return [value for value in values if isinstance(value, set)]


def filter_dictionaries(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dictionaries
    >>> filter_dictionaries([1, 2, 3, 3.6, 'abc', {}, [