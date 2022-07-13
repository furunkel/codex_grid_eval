
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    """
    return [x for x in values if isinstance(x, int)]


@curry
def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none([None, '', 3.14, None, 5.0])
    [None, 5.0]
    """
    return [x for x in values if x is not None]


@curry
def filter_number(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for numbers
    >>> filter_number(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, (int, float))]


@curry
def filter_string(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for strings
    >>> filter_string(['a', 3.14, None, 5.0])
    ['a', 3.14, 5.0]
    """
    return [x for x in values if isinstance(x, str)]


@curry
def filter_dict(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dicts
    >>> filter_dict(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, dict)]


@curry
def filter_sequence(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for sequences
    >>> filter_sequence(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, Sequence)]


@curry
def filter_set(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for sets
    >>> filter_set(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, Set)]


@curry
def filter_union(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for unions
    >>> filter_union(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, Union)]


@curry
def filter_union_of_tuples(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for unions of tuples
    >>> filter_union_of_tuples(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, (tuple, list))]


@curry
def filter_union_of_lists(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for unions of lists
    >>> filter_union_of_lists(['a', 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, (list, tuple))]


@curry
def filter_union_of_