
def incr_list(l: list):
    """Return list with elements incremented by 100.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [105, 103, 105, 102, 103, 103, 109, 100, 223]
    """
    return [x + 100 for x in l]


def incr_dict(d: dict):
    """Return dict with elements incremented by 100.
    >>> incr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 101, 'b': 102, 'c': 103}
    """
    return {k: x + 100 for k, v in d.items()}


def decr_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict({'a': 101, 'b': 102, 'c': 103})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: x - 100 for k, v in d.items()}


def decr_dict_by_key(
        d: dict, key: str, decr_key: str, decr_amount: int
):
    """Return dict with elements decremented by amount.
    >>> decr_dict_by_key({'a': 101, 'b': 102, 'c': 103}, 'a', 'c', -2)
    {'a': -1, 'b': 2, 'c': 3}
    """
    return {
        k: v - decr_amount
        for k, v in d.items()
        if k == decr_key and v >= decr_amount
    }


def decr_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list([105, 103, 105, 102, 103, 103, 109, 100, 223])
    [5, 3, 5, 2, 3, 3, 9, 0, 122]
    """
    return [x - 100 for x in l]


def decr_list_by_key(
        l: list, key: str, decr_key: str, decr_amount: int
):
    """Return list with elements decremented by amount.
    >>> decr_list_by_key([5, 3, 5, 2, 3, 3, 9, 0, 122], "a", -2)
    [5, 3, 5, 2, 3, 3, 9, 0, 122]
    """
    return [
        x - decr_amount
        for x in l
        if x == decr_key and x >= decr_amount
    ]


def decr_dict(d: dict):
    """Return dict with elements decremented by 100.
    >>> decr_dict({'a': 101, 'b': 102, 'c': 103})
    {'a': -1, 'b': 2, 'c': -3}
    """
    return {k: v - 100 for k, v in d.items()}


def decr_dict_by_key(
        d: dict, key: str, decr_key: str, decr_amount: int
):
    """Return dict with elements decremented by amount.
    >>> decr_dict_by_key({'a': 101, 'b': 102, 'c': 103}, 'a', 'c', -2)
    {'a': -1, 'b': 2, 'c': -3}
    """
    return {
        k: v - decr_amount
        for k, v in d.items()
        if k == decr_key and v