def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [str(value) for value in values if value]


def filter_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values(['a', 3.14, 5])
    ['a', 3.14]
    """
    return [str(value) for value in values if value]


def filter_values_with_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_with_none(['a', 3.14, 5])
    ['a']
    """
    return [str(value) for value in values if value]


def filter_values_with_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_with_empty([])
    []
    """
    return []


def filter_values_with_none_and_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_with_none_and_empty(['a', 3.14, 5])
    ['a']
    """
    return []


def filter_values_with_empty_and_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_with_empty_and_none(['a', 3.14, 5])
    ['a']
    """
    return []


def filter_values_with_none_and_empty_and_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_with_none_and_empty_and_none(['a', 3.14, 5])
    ['a']
    """
    return []


def filter_values_with_empty_and_none_and_empty(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>>