
def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3.6]
    """

def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [3]
    """

def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """

def filter_strings_with_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """

def filter_strings_with_empty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """

def filter_strings_with_empty_strings_with_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_strings_with_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """

def filter_strings_with_empty_strings_with_empty_strings_with_none(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_empty_strings_with_empty_strings_with_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """

def filter_strings_with_empty