
def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    """

def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints(['a', 3, 5])
    [3]
    """

def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3, 5])
    ['a', 3, 5]
    """

def filter_strings_with_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_none(['a', 3, 5])
    ['a', 3, 5]
    """

def filter_strings_with_empty(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty(['a', 3, 5])
    []
    """

def filter_strings_with_none_and_empty(values: List[Any], empty_string: str) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_none_and_empty(['a', 3, 5])
    ['a', 3, 5]
    """

def filter_strings_with_empty_and_none(values: List[Any], empty_string: str) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_and_none(['a', 3, 5])
    ['a', 3, 5]
    """

def filter_strings_with_empty_and_none_and_empty(values: List[Any], empty_string: str) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_and_none_and_empty(['a', 3, 5])
    ['a', 3, 5]
    """

def filter_strings_with_none_and_empty_