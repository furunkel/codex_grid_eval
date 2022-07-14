def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    """
    return [v for v in values if v]


def filter_dicts(values: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Filter given dict of any python values only for dicts
    >>> filter_dicts({'a': 3.14, 5: 'a'})
    {'a': 3.14, '5': 'a'}
    """
    return {k: v for k, v in values.items() if v}


def filter_lists_with_none(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists_with_none([])
    []
    """
    return [v for v in values if v]


def filter_dicts_with_none(values: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Filter given dict of any python values only for dicts
    >>> filter_dicts_with_none({})
    {}
    """
    return {k: v for k, v in values.items() if v}


def filter_lists_with_none(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists_with_none([])
    []
    """
    return [v for v in values if v]


def filter_dicts_with_none(values: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Filter given dict of any python values only for dicts
    >>> filter_dicts_with_none({})
    {}
    """
    return {k: v for k, v in values.items() if v}


def filter_lists_with_none(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists_with_none([])
    []
    """
    return [v for v in values if v]


def filter_dicts_with_none(values: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Filter given dict of any python values only for dicts
    >>> filter_dicts_with