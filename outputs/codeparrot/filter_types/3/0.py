
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3]
    """

def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """

def filter_strings_with_numbers(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings_with_numbers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """

def filter_strings_with_strings_and_numbers(values: List[Any], values_and_numbers: List[str]) -> List[str]:
    """ Filter given list of any python values only for strings and numbers
    >>> filter_strings_with_strings_and_numbers([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """

def filter_strings_with_strings_and_numbers_and_strings(values: List[Any], values_and_numbers: List[str], values_and_strings: List[str]) -> List[str]:
    """ Filter given list of any python values only for strings and numbers and strings
    >>> filter_strings_with_strings_and_numbers_and_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc', 'abc']
    """

def filter_strings_with_strings_and_numbers_and_strings_and_strings_and_numbers(values: List[Any], values_and_numbers: List[str], values_and_strings: List[str], values_and_numbers: List[str]) -> List[str]:
    """ Filter given list of any python values only for strings and numbers and strings and strings and numbers and strings and numbers and strings and numbers and strings and numbers and strings and numbers and strings and numbers