
def filter_dictionarys(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionarys
    >>> filter_dictionarys(['a', 3.14, 5])
    []
    """
    return [x for x in values if isinstance(x, dict)]


def filter_null_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for null
    >>> filter_null_values(['a', 3.14, None, 5.0])
    ['a', 3.14, 5.0]
    """
    return [x for x in values if x is not None]


def filter_out_none_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for null
    >>> filter_out_none_values(['a', 3.14, None, 5.0])
    ['a', 3.14, 5.0]
    """
    return [x for x in values if x is not None and x != '']


def flatten_list(list_of_lists: List[List[Any]]) -> List[Any]:
    """ Flatten given list of lists
    >>> flatten_list([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    """
    return [item for sublist in list_of_lists for item in sublist]


def flatten_dicts(list_of_dicts: List[Dict[Any, Any]]) -> List[Any]:
    """ Flatten given list of dictionaries
    >>> flatten_dicts([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    """
    return [item for sublist in list_of_dicts for item in sublist]


def flatten_dict(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Flatten given dictionary
    >>> flatten_dict({'a': 1, 'b': 2})
    {'a': 1, 'b': 2}
    """
    return {k: v for k, v in dictionary.items()}


def unflatten_dict(flattened: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Unflatten given dictionary
    >>> unflatten_dict([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    """
    return {k: v for sublist in flattened for k, v in sublist.items()}


def unflatten_list(flattened: List[Any]) -> List[Any]:
    """ Unflatten given list
    >>> unflatten_list([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    """
    return [item for sublist in flattened for item in sublist]


def unflatten_dict(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    """ Unflatten given dictionary
    >>> unflatten_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    """
    return {k: v for sublist in dictionary.values() for k, v in sublist.items()}


def unflatten_list_dict(flattened: List[Any]) -> List[Dict[Any, Any]]:
    """ Unflatten given list of dictionaries
    >>> unflatten_list_dict([{'a': 1, 'b': 2}, {'c': 3, 'd