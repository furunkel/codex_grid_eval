
def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    """
    return [float(v) for v in values if isinstance(v, float)]


def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints(['a', 3.14, 5])
    [3, 5]
    """
    return [int(v) for v in values if isinstance(v, int)]


def filter_strs(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strs(['a', 3.14, 5])
    ['a', 3.14, 5]
    """
    return [v for v in values if isinstance(v, str)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none(['a', 3.14, 5])
    [None, 3.14, 5]
    """
    return [v for v in values if v is not None]


def filter_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for empty strings
    >>> filter_empty(['', 'a', ''])
    ['', 'a']
    """
    return [v for v in values if v != ""]


def filter_not_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for non-empty strings
    >>> filter_not_empty(['', 'a', ''])
    ['a', '']
    """
    return [v for v in values if v != ""]


def filter_dict(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dict(['a', {'b': 'c'}])
    [{'b': 'c'}]
    """
    return [dict(v) for v in values if isinstance(v, dict)]


def filter_dict_keys(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dict keys
    >>> filter_dict_keys(['a', {'b': 'c'}])
    ['a', {'b': 'c'}]
    """
    return [dict(v)[k] for v in values if isinstance(v, dict)]


def filter_dict_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dict values
    >>> filter_dict_values(['a', {'b': 'c'}])
    ['a', {'b': 'c'}]
    """
    return [dict(v)[v] for v in values if isinstance(v, dict)]


def filter_dict_items(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dict items
    >>> filter_dict_items(['a', {'b': 'c'}])
    ['a', {'b': 'c'}]
    """
    return [dict(v)[k] for v in values if isinstance(v, dict)]


def filter_dict_items(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for dict items
    >>> filter_