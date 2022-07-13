
def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3.14, 5])
    ['a']
    """
    return [value for value in values if isinstance(value, str)]


def filter_strings_with_length(values: List[Any], length: int) -> List[str]:
    """ Filter given list of any python values only for strings with given length
    >>> filter_strings_with_length(['a', 3.14, 5, 'abc'], 3)
    ['abc']
    """
    return [value for value in values if isinstance(value, str) and len(value) == length]


def filter_strings_with_length_and_contains(values: List[Any], length: int, contains: str) -> List[str]:
    """ Filter given list of any python values only for strings with given length and contains given string
    >>> filter_strings_with_length_and_contains(['a', 3.14, 5, 'abc'], 3, 'b')
    ['abc']
    """
    return [value for value in values if isinstance(value, str) and len(value) == length and contains in value]


def filter_strings_with_length_and_contains_and_starts_with(values: List[Any], length: int, contains: str,
                                                            starts_with: str) -> List[str]:
    """ Filter given list of any python values only for strings with given length and contains given string and
    starts with given string
    >>> filter_strings_with_length_and_contains_and_starts_with(['a', 3.14, 5, 'abc'], 3, 'b', 'a')
    ['abc']
    """
    return [value for value in values if isinstance(value, str) and len(value) == length and contains in value and
            value.startswith(starts_with)]


def filter_strings_with_length_and_contains_and_starts_with_and_ends_with(values: List[Any], length: int, contains: str,
                                                                          starts_with: str, ends_with: str) -> List[str]:
    """ Filter given list of any python values only for strings with given length and contains given string and
    starts with given string and