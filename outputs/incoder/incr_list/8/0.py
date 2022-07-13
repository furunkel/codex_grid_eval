
def incr_list(l: list):
    """Return list with elements incremented by 9999.
    >>> incr_list([1, 2, 3])
    [10000, 10001, 10002]
    """
    return [x + 9999 for x in l]


def incr_dict(d: dict):
    """Return dict with elements incremented by 9999.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 10000, 'b': 10001, 'c': 10002}
    """
    return {k: x + 9999 for k, v in d.items()}


def decr_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict({'a': 10000, 'b': 10001, 'c': 10002})
    {'a': -1, 'b': 2, 'c': -1}
    """
    return {k: x - 9999 for k, v in d.items()}


def decr_list(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list([1, 2, 3])
    [-1, 2, -3]
    """
    return [x - 9999 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict({'a': -1, 'b': 2, 'c': -3})
    {'a': 10000, 'b': 10001, 'c': 10002}
    """
    return {k: x - 9999 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: str, decr_key: str, decr_value: Union[int, float]
) -> dict:
    """Return dict with elements decremented by 9999.
    >>> decr_dict_by_key({'a': -1, 'b': 2, 'c': -3}, 'a', 'c', 1000)
    {'a': 10000, 'b': 10001, 'c': 10002}
    """
    return {
        k: decr_value if k == decr_key else x - 9999
        for k, v in d.items()
    }


def decr_list_by_key(
    l: list, key: str, decr_key: str, decr_value: Union[int, float]
) -> list:
    """Return list with elements decremented by 9999.
    >>> decr_list_by_key([1, 2, 3], 1, 'c', 1000)
    [10000, 10001, 10002]
    """
    return [x - 9999 for x in l if x == decr_value]


def decr_dict_by_key_list(
    d: dict, key: str, decr_key: str, decr_value: Union[int, float]
) -> dict:
    """Return dict with elements decremented by 9999.
    >>> decr_dict_by_key_list({'a': -1, 'b': 2, 'c': -3}, 'a', 'c', 1000)
    {'a': 10000, 'b': 10001, 'c': 10002}
    """
    return {
        k: decr_value if k == decr_key else x - 9999
        for k, v in d.items()
    }


def decr_list_by_key_list(
    l: list, key: str, decr_key: str, decr_value: Union[int, float]
) -> list:
    """Return list with elements decremented by 