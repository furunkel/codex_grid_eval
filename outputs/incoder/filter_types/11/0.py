
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """
    return list(filter(lambda v: isinstance(v, tuple), values))


def filter_list(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for list
    >>> filter_list([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {}, []]
    """
    return list(filter(lambda v: isinstance(v, list), values))


def filter_dict(values: List[Any]) -> Dict[Any, Any]:
    """ Filter given list of any python values only for dict
    >>> filter_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3.6, 'e': 'abc', 'f': {}, 'g': [], 'h': [(1,)]})
    {'a': 1, 'b': 2, 'c': 3, 'd': 3.6, 'e': 'abc', 'f': {}, 'g': [], 'h': [(1,)]}
    """
    return dict(filter(lambda v: isinstance(v, dict), values))


def filter_set(values: List[Any]) -> Set[Any]:
    """ Filter given list of any python values only for set
    >>> filter_set({'a': 1, 'b': 2, 'c': 3, 'd': 3.6, 'e': 'abc', 'f': {}, 'g': [], 'h': [(1,)]})
    {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    """
    return set(filter(lambda v: isinstance(v, set), values))


def filter_str(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for str
    >>> filter_str(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    return list(filter(lambda v: isinstance(v, str), values))


def filter_int(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for int
    >>> filter_int([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return list(filter(lambda v: isinstance(v, int), values))


def filter_float(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for float
    >>> filter_float([1.0, 2.0, 3.0, 3.6, 'abc', {}, [], (1,)])
    [1.0, 2.0, 3.0]
    """
    return list(filter(lambda v: isinstance(v, float), values))


def filter_bool(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for bool
    >>> filter_bool([True, False, True, True, True, True, True, True])
    [True, False, True]
    """
    return list(filter(lambda v: isinstance(v, bool), values))


def filter_none(values: List[Any]) -> List[None]:
    """ Filter given list of any python values only for none
    >>> filter_none([None, True, None, False])
    [None, False]
    """
    return list(filter(lambda v: v is None, values))


def filter_any(values: List[