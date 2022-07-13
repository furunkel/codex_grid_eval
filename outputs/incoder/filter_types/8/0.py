
def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    """
    return [x for x in values if isinstance(x, list)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for none
    >>> filter_none([None, 3.14, 5])
    [None, 3.14, 5]
    """
    return [x for x in values if x is not None]


def filter_dict(values: List[Any]) -> List[Dict[str, str]]:
    """ Filter given list of any python values only for dict
    >>> filter_dict(['a', 3.14, 5])
    []
    """
    return [dict(x.items()) for x in values if isinstance(x, dict)]


def filter_dict_keys(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for dict keys
    >>> filter_dict_keys(['a', 3.14, 5])
    []
    """
    return [key for key in values if isinstance(key, str)]


def filter_dict_values(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for dict values
    >>> filter_dict_values(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, str)]


def filter_dict_items(values: List[Any]) -> List[Tuple[str, str]]:
    """ Filter given list of any python values only for dict items
    >>> filter_dict_items(['a', 3.14, 5])
    []
    """
    return [item for item in values if isinstance(item, tuple)]


def filter_dict_items_values(values: List[Any]) -> List[Tuple[str, str]]:
    """ Filter given list of any python values only for dict items values
    >>> filter_dict_items_values(['a', 3.14, 5])
    []
    """
    return [item for item in values if isinstance(item, tuple)]


def filter_dict_items_keys(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for dict items keys
    >>> filter_dict_items_keys(['a', 3.14, 5])
    []
    """
    return [key for key in values if isinstance(key, str)]


def filter_dict_items_items_values(values: List[Any]) -> List[Tuple[str, str]]:
    """ Filter given list of any python values only for dict items items values
    >>> filter_dict_items_items_values(['a', 3.14, 5])
    []
    """
    return [item for item in values if isinstance(item, tuple)]


def filter_dict_items_items_keys(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for dict items items keys
    >>> filter_dict_items_items_keys(['a', 3.14, 5])
    []
    """
    return [key for key in values if isinstance(key, str)]


def filter_dict_items_items_items_values(values: List[Any]) -> List[Tuple[str, str]]:
    """ Filter given list of any python values only for dict items items values
    >>> filter_dict_items_items_items_values(['a', 3.14, 5])
    []
    """
    return [item for item in value