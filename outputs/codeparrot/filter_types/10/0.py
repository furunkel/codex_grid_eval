def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    """
    return [tuple(value) for value in values if value]


def filter_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts(['a', 3.14, 5])
    {'a': 3.14, 'b': 5}
    """
    return [dict(value) for value in values if value]


def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [list(value) for value in values if value]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none(['a', 3.14, 5])
    []
    """
    return [value for value in values if value]


def filter_none_or_str(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none_or_str(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [value for value in values if value]


def filter_none_or_list(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none_or_list(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [value for value in values if value]


def filter_none_or_dict(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dicts
    >>> filter_none_or_dict(['a', 3.14, 5])
    {'a': 3.14, 'b': 5}
    """
    return [value for value in values if value]


def filter_none_or_none(values: List[Any]) -> List[