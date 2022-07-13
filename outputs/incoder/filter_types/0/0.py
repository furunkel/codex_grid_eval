
def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [x for x in values if isinstance(x, str)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none([None, 3.14, None, 5.0])
    [None, 3.14, None]
    """
    return [x for x in values if x is not None]


def filter_numeric(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for numeric
    >>> filter_numeric([None, 3.14, None, 5.0])
    [3.14, 5.0]
    """
    return [x for x in values if isinstance(x, (int, float))]


def filter_datetime(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for datetime
    >>> filter_datetime([None, 3.14, None, 5.0])
    [datetime.datetime(2019, 2, 24, 13, 36, 10), datetime.datetime(2019, 2, 24, 13, 36, 10)]
    """
    return [x for x in values if isinstance(x, datetime.datetime)]


def filter_date(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for date
    >>> filter_date([None, 3.14, None, 5.0])
    [datetime.date(2019, 2, 24), datetime.date(2019, 2, 24)]
    """
    return [x for x in values if isinstance(x, datetime.date)]


def filter_time(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for time
    >>> filter_time([None, 3.14, None, 5.0])
    [datetime.time(13, 36, 10), datetime.time(13, 36, 10)]
    """
    return [x for x in values if isinstance(x, datetime.time)]


def filter_boolean(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for boolean
    >>> filter_boolean([None, 3.14, None, 5.0])
    [True, False]
    """
    return [x for x in values if isinstance(x, bool)]


def filter_dict(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dict
    >>> filter_dict([None, 3.14, None, 5.0])
    [{'a': 3.14, 'b': 5.0}]
    """
    return [x for x in values if isinstance(x, dict)]


def filter_sequence(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for sequence
    >>> filter_sequence(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, (list, tuple))]


def filter_set(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for set
    >>> filter_set(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [x for x in values if isinstance(x, (set, frozenset))]


def filter_nones(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_nones(['a', 3.14, None, 5.0])
    ['a', 3.14, None, 5.0]