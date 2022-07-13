
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [(1,)]
    """

def filter_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_dicts([{'a': 1}, {'b': 2}])
    [{'a': 1}, {'b': 2}]
    """

def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {}]
    """

def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for lists
    >>> filter_none([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    []
    """

def filter_none_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_none_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    []
    """

def filter_none_dicts(values: List[Any]) -> List[Dict]:
    """ Filter given list of any python values only for dicts
    >>> filter_none_dicts([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {}]
    """

def filter_none_lists_and_dicts(values: List[Any],
                                    key: str) -> List[List[Any]]:
    """ Filter given list of any python values only for lists and dicts
    >>> filter_none_lists_and_dicts([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [1, 2, 3, 3.6, 'abc', {}]
    """

def filter_none_dicts_and_lists(values: List[Any],