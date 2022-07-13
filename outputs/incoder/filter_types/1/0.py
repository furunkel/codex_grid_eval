
def filter_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for strings
    >>> filter_strings([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    ['abc']
    """
    return [x for x in values if isinstance(x, str)]


@curry
def filter_booleans(values: List[Any]) -> List[bool]:
    """ Filter given list of any python values only for booleans
    >>> filter_booleans([True, True, True, True, True, True, True, True])
    [True]
    """
    return [x for x in values if isinstance(x, bool)]


@curry
def filter_none(values: List[Any]) -> List[None]:
    """ Filter given list of any python values only for none
    >>> filter_none([None, None, None])
    [None]
    """
    return [x for x in values if x is None]


@curry
def filter_none_or(values: List[Any]) -> List[None]:
    """ Filter given list of any python values only for none
    >>> filter_none_or([None, None, None])
    [None]
    """
    return [x for x in values if x is None]


@curry
def filter_empty(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for empty
    >>> filter_empty([None, '', {}, [], (1,)])
    ['']
    """
    return [x for x in values if x != ""]


@curry
def filter_nonempty(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for nonempty
    >>> filter_nonempty([None, '', {}, [], (1,)])
    ['']
    """
    return [x for x in values if x != ""]


@curry
def filter_nonempty_strings(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for nonempty strings
    >>> filter_nonempty_strings([None, '', {}, [], (1,)])
    ['']
    """
    return [x for x in values if x != ""]


@curry
def filter_nonempty_strings_or_empty(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for nonempty strings
    >>> filter_nonempty_strings_or_empty([None, '', {}, [], (1,)])
    ['']
    """
    return [x for x in values if x != ""]


@curry
def filter_nonempty_strings_or_empty_list(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for nonempty strings
    >>> filter_nonempty_strings_or_empty_list([None, '', {}, [], (1,)])
    ['']
    """
    return [x for x in values if x != ""]


@curry
def filter_nonempty_strings_or_empty_dict(values: List[Any]) -> List[str]:
    """ Filter given list of any python values only for nonempty strings
    >>> filter_nonempty_strings_or_empty_dict([None, '', {}, [], (1,)])
    ['']
    """