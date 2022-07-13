
def incr_list(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [10004, 10002, 10004, 10001, 10002, 10002, 10008, 9999, 10122]
    """
    return [x + 9999 for x in l]


def incr_dict(d: dict):
    """Return dict with elements incremented by 9999.
    >>> incr_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10})
    {'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}
    """
    return {x: x + 9999 for x in d.keys()}


def incr_dict_list(dict_list: list):
    """Return list with elements incremented by 9999.
    >>> incr_dict_list([{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}, {'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}])
    [{'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}, {'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}]
    """
    return [{x: x + 9999 for x in d.keys()} for d in dict_list]


def incr_dict_dict(dict_dict: dict):
    """Return dict with elements incremented by 9999.
    >>> incr_dict_dict({'a': {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}, 'b': {'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}})
    {'a': {'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}, 'b': {'a': 10004, 'b': 10002, 'c': 10004, 'd': 10001, 'e': 10002, 'f': 10002, 'g': 10008, 'h': 9999, 'i': 10122}}
    """
    return {k: 