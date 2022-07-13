
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    """
    return [x for x in values if isinstance(x, tuple)]


def filter_list(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_list(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, list)]


def filter_dict(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dicts
    >>> filter_dict(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, dict)]


def filter_set(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for sets
    >>> filter_set(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, set)]


def filter_str(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for strings
    >>> filter_str(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, str)]


def filter_int(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for ints
    >>> filter_int(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, int)]


def filter_float(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for floats
    >>> filter_float(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, float)]


def filter_bool(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for bools
    >>> filter_bool(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, bool)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if x is None]


def filter_any(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for any values
    >>> filter_any(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return values


def filter_all(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for all values
    >>> filter_all(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return values


def filter_none_or(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for none or any values
    >>> filter_none_or(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return list(filter(lambda x: x 