def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
    """
    return [v for v in values if v]


def filter_dicts(values: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Filter given dict of any python values only for dicts
    >>> filter_dicts({1: 'abc', 2: 'def'})
    {'abc': 'def'}
    """
    return {v: v for v in values if v}


def filter_none(values: Any) -> Any:
    """ Filter given None values only for lists
    >>> filter_none({})
    []
    """
    return {v: v for v in values if v}


def filter_none_or_str(values: Any) -> Any:
    """ Filter given None or a string value only for lists
    >>> filter_none_or_str({})
    ''
    """
    return {v: v for v in values if v}


def filter_none_or_list(values: Any) -> Any:
    """ Filter given None or a list value only for lists
    >>> filter_none_or_list([])
    []
    """
    return {v: v for v in values if v}


def filter_none_or_dict(values: Any) -> Any:
    """ Filter given None or a dict value only for lists
    >>> filter_none_or_dict({})
    {}
    """
    return {v: v for v in values if v}


def filter_none_or_none(values: Any) -> Any:
    """ Filter given None or a None value only for lists
    >>> filter_none_or_none({})
    None
    """
    return {v: v for v in values if v}


def filter_none_or_str(values: Any) -> Any:
    """ Filter given None or a string value only for lists
    >>> filter_none_or_str({})
    ''
    """
    return {v: v for v in values if v}


def filter_none_or_list(values: Any) -> Any:
    """ Filter given None or a list value only for lists
    >>> filter_none_or_