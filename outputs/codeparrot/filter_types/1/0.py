def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(value) for value in values if value]


def filter_values(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(value) for value in values if value]


def filter_values_by_regex(values: List[Any], regex: str) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_by_regex([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(value) for value in values if re.search(regex, value)]


def filter_values_by_regex_and_ignore(values: List[Any], regex: str, ignore_case: bool = False) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_by_regex_and_ignore([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(value) for value in values if re.search(regex, value)]


def filter_values_by_regex_and_ignore_case(values: List[Any], regex: str, ignore_case: bool = False) -> List[Any]:
    """ Filter given list of any python values only for values
    >>> filter_values_by_regex_and_ignore_case([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [str(value) for value in values if re.search(regex, value)]


def filter_values_by_regex_and_ignore_case_and_ignore(values: List[Any], regex: str, ignore_case: bool = False) -> List[Any]:
    """ Filter given list