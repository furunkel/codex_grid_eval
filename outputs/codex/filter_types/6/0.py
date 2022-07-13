
def filter_dictionarys(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionarys
    >>> filter_dictionarys(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, dict)]


def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, list)]


def filter_tuples(values: List[Any]) -> List[Tuple[Any, ...]]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
    """
    return [value for value in values if isinstance(value, tuple)]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [value for value in values if isinstance(value, str)]


def filter_numbers(values: List[Any]) -> List[Union[int, float]]:
    """ Filter given list of any python values only for numbers
    >>> filter_numbers(['a', 3.14, 5])
    [3.14, 5]
    """
    return [value for value in values if isinstance(value, (int, float))]


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    """
    return [value for value in values if isinstance(value, int)]


def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    """
    return [value for value in values if isinstance(value, float)]


def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for boole