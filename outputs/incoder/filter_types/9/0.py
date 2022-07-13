
def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
    """
    return [x for x in values if isinstance(x, list)]


def filter_none(values: List[Any]) -> List[Any]:
    """ Filter given list of any python values only for None
    >>> filter_none([None, 1, None, 3.6, 'abc', {}, [], (1,)])
    [None, 1, None, 3.6, 'abc', {}, [], (1,)]
    """
    return [x for x in values if x is not None]


def filter_dict(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dicts
    >>> filter_dict([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}, {'a': 7, 'b': 8}, {'a': 9, 'b': 10}, {'a': 11, 'b': 12}, {'a': 13, 'b': 14}, {'a': 15, 'b': 16}, {'a': 17, 'b': 18}, {'a': 19, 'b': 20}, {'a': 21, 'b': 22}, {'a': 23, 'b': 24}, {'a': 25, 'b': 26}, {'a': 27, 'b': 28}, {'a': 29, 'b': 30}, {'a': 31, 'b': 32}, {'a': 33, 'b': 34}, {'a': 35, 'b': 36}, {'a': 37, 'b': 38}, {'a': 39, 'b': 40}, {'a': 41, 'b': 42}, {'a': 43, 'b': 44}, {'a': 45, 'b': 46}, {'a': 47, 'b': 48}, {'a': 49, 'b': 50}, {'a': 51, 'b': 52}, {'a': 53, 'b': 54}, {'a': 55, 'b': 56}, {'a': 57, 'b': 58}, {'a': 59, 'b': 60}, {'a': 61, 'b': 62}, {'a': 63, 'b': 64}, {'a': 65, 'b': 66}, {'a': 67, 'b': 68}, {'a': 69, 'b': 70}, {'a': 71, 'b': 72}, {'a': 73, 'b': 74}, {'a': 75, 'b': 76}, {'a': 77, 'b': 78}, {'a': 79, 'b': 80}, {'a': 81, 'b': 82}, {'a': 83, 'b': 84}, {'a': 85, 'b': 86}, {'a': 87, 'b': 88}, {'a': 89, 'b': 90}, {'a': 91, 'b': 92}, {'a': 93, 'b': 94}, {'a': 95, 'b': 96}, {'a': 97, 'b': 98}, {'a': 99, 'b': 100}, {'a': 101, 'b': 102}, {'a': 103, 'b': 104}, {'a': 105, 'b': 106}, {'a': 107, 'b': 108}, {'a': 109, 'b': 110}, {'a': 111, 'b': 112}, {'a': 113, 'b': 114}, {'a': 115, 'b': 116}, {'a': 117, 'b': 118}, {'a': 119, '