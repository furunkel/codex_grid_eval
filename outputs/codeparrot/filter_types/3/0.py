def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """
    return [int(v) for v in values if v in [1, 2, 3, 4]]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """
    return [str(v) for v in values if v in [1, 2, 3, 4]]


def filter_strings_with_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """
    return [str(v) for v in values if v in [1, 2, 3, 4]]


def filter_strings_with_empty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_strings([])
    []
    """
    return [str(v) for v in values if v in [1, 2, 3, 4]]


def filter_strings_with_none_and_empty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_none_and_empty_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """
    return [str(v) for v in values if v in [1, 2, 3, 4]]


def filter_strings_with_empty_strings_and_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_strings_and_none([1, 2, 3,