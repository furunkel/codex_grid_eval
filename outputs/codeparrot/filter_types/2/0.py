def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    """
    return [int(v) for v in values if v in [0, 1, 2, 3, 4]]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 'b', 'c'])
    ['a', 'b', 'c']
    """
    return [str(v) for v in values if v in [0, 1, 2, 3, 4]]


def filter_strings_with_numbers(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_numbers(['a', 'b', 'c'])
    ['a', 'b', 'c']
    """
    return [str(v) for v in values if v in [0, 1, 2, 3, 4]]


def filter_strings_with_strings_and_numbers(values: List[Any], values_and_numbers: List[str]) -> List[str]:
    """ Filter given list of any python values only for strings and numbers
    >>> filter_strings_with_strings_and_numbers(['a', 'b', 'c'])
    ['a', 'b', 'c']
    """
    return [str(v) for v in values_and_numbers if v in [0, 1, 2, 3, 4]]


def filter_strings_with_strings_and_numbers_and_strings(values: List[Any], values_and_numbers: List[str], values_and_strings: List[str]) -> List[str]:
    """ Filter given list of any python values only for strings and numbers and strings
    >>> filter_strings_with_strings_and_numbers(['a', 'b', 'c'])
    ['a', 'b', 'c']
    """
    return [str(v) for v in values_and_numbers if v in [0, 1, 2, 3, 4]] + [str(v) for v in values_and_strings if v in [0, 1, 2, 3, 4