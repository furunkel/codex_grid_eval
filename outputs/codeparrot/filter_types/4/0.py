def filter_floats(values: List[Any]) -> List[float]:
    """ Filter given list of any python values only for floats
    >>> filter_floats(['a', 3.14, 5])
    [3.14]
    """
    return [float(v) for v in values if v is not None]


def filter_ints(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for ints
    >>> filter_ints(['a', 3, 5])
    [3]
    """
    return [int(v) for v in values if v is not None]


def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings(['a', 3, 5])
    ['a', 3, 5]
    """
    return [str(v) for v in values if v is not None]


def filter_strings_or_ints(values: List[Any], allow_none: bool = False) -> List[str]:
    """ Filter given list of any python values only for strings or ints
    >>> filter_strings_or_ints(['a', 3, 5])
    ['a', 3, 5]
    >>> filter_strings_or_ints(None)
    []
    >>> filter_strings_or_ints(None, allow_none=True)
    []
    >>> filter_strings_or_ints(None, allow_none=False)
    []
    >>> filter_strings_or_ints(None, allow_none=True)
    []
    >>> filter_strings_or_ints(None, allow_none=False)
    []
    """
    if allow_none:
        return []
    return [str(v) for v in values if v is not None]


def filter_strings_or_ints_or_strings(values: List[Any], allow_none: bool = False) -> List[str]:
    """ Filter given list of any python values only for strings or ints
    >>> filter_strings_or_ints_or_strings(['a', 3, 5])
    ['a', 3, 5]
    >>> filter_strings_or_ints_or_strings(None)
    []
    >>> filter_strings_or_ints_or_strings(None, allow_none=True)
    []
   