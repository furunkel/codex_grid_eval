
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_integers_and_strings(values: List[Any]) -> List[Union[int, str]]:
    """ Filter given list of any python values only for integers and strings
    >>> filter_integers_and_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 'abc']
    """
    return [value for value in values if isinstance(value, (int, str))]


def filter_integers_and_strings_and_lists(values: List[Any]) -> List[Union[int, str, List[Any]]]:
    """ Filter given list of any python values only for integers, strings and lists
    >>> filter_integers_and_strings_and_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 'abc', []]
    """
    return [value for value in values if isinstance(value, (int, str, list))]


def filter_integers_and_strings_and_lists_and_dicts(values: List[Any]) -> List[Union[int, str, List[Any], Dict[Any, Any]]]:
    """ Filter given list of any python values only for integers, strings, lists and dictionaries
    >>> filter_integers_and_strings_and_lists_and_dicts([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 'abc', [], {}]
    """
    return [value for value in values if isinstance(value, (int, str, list, dict))]


def filter_integers_and_strings_and_lists_and_dicts_and_tuples(values: List[Any]) -> List[Union[int, str, List[Any], Dict[Any, Any], Tuple[Any, ...]]]:
    """ Filter given list of any python values only for integers, strings, lists, dictionaries and tuples
    >>> filter_integers_and_strings_and_lists_