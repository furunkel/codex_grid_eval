
def incr_list(l: list):
    """Return list with elements incremented by 0.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x + 1 for x in l]


def decr_list(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [5, 3, 5, 2, 3, 3, 9, 0, 123]
    """
    return [x - 1 for x in l]


def incr_dict(d: dict):
    """Return dict with elements incremented by 0.
    >>> incr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: v + 1 for k, v in d.items()}


def decr_dict(d: dict):
    """Return dict with elements decremented by 0.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: v - 1 for k, v in d.items()}


def incr_dict_by_key(
    d: dict,
    key: str,
    increment: int,
    default: Any = None,
) -> Any:
    """Return dict with elements incremented by 0.
    >>> incr_dict_by_key({'a': 1, 'b': 2, 'c': 3}, 'b', 2, default=0)
    {'a': 1, 'b': 3, 'c': 3}
    """
    if key in d:
        d[key] += increment
    else:
        d[key] = default
    return d[key]


def decr_dict_by_key(
    d: dict,
    key: str,
    decrement: int,
    default: Any = None,
) -> Any:
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3}, 'b', 2, default=0)
    {'a': 1, 'b': 2, 'c': 3}
    """
    if key in d:
        d[key] -= decrement
    else:
        d[key] = default
    return d[key]


def incr_dict_by_key_with_default(
    d: dict,
    key: str,
    increment: int,
    default: Any = None,
) -> Any:
    """Return dict with elements incremented by 0.
    >>> incr_dict_by_key_with_default({'a': 1, 'b': 2, 'c': 3}, 'b', 2, default=0)
    {'a': 1, 'b': 3, 'c': 3}
    """
    if key in d:
        d[key] += increment
    else:
        d[key] = default
    return d[key]


def decr_dict_by_key_with_default(
    d: dict,
    key: str,
    decrement: int,
    default: Any = None,
) -> Any:
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key_with_default({'a': 1, 'b': 2, 'c': 3}, 'b', 2, default=0)
    {'a': 1, 'b': 2, 'c': 3}
    """
    if key in d:
        d[key] -= decrement
    else:
        d[key] = default
    return d[key]


def 