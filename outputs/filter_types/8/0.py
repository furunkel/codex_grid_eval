
def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, list)]


def filter_numbers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for numbers
    >>> filter_numbers(['a', 3.14, 5])
    [3.14, 5]
    """
    return [value for value in values if isinstance(value, (int, float))]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [value for value in values if isinstance(value, str)]


def filter_unique(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for unique values
    >>> filter_unique([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """
    return list(set(values))


def filter_unique_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for unique strings
    >>> filter_unique_strings(['a', 'b', 'c', 'a', 'b', 'c'])
    ['a', 'b', 'c']
    """
    return list(set(filter_strings(values)))


def filter_unique_numbers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for unique numbers
    >>> filter_unique_numbers([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """
    return list(set(filter_numbers(values)))


def filter_unique_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for unique lists
    >>> filter_unique_lists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6