
def incr_list(l: list):
    """Return list with elements incremented by 0.
    >>> incr_list([1, 2, 3])
    [1, 2, 3]
    """
    return [x + 1 for x in l]


def decr_list(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list([1, 2, 3])
    [3, 2, 1]
    """
    return [x - 1 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 0.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3})
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
        d: dict, keys: list, default=None
):
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3}, ['a', 'b'])
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items() if k in keys}


def decr_dict_by_key_with_default(
        d: dict, keys: list, default=None
):
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key_with_default({'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], 0)
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items() if k in keys}


def decr_dict_by_key_with_default_and_default(
        d: dict, keys: list, default=None
):
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key_with_default_and_default(
            {'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], 0, default='default'
    )
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items() if k in keys}


def decr_dict_by_key_with_default_and_default_and_default(
        d: dict, keys: list, default=None
):
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key_with_default_and_default_and_default(
            {'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], 0, default='default'
    )
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items() if k in keys}


def decr_dict_by_key_with_default_and_default_and_default_and_default(
        d: dict, keys: list, default=None
):
    """Return dict with elements decremented by 0.
    >>> decr_dict_by_key_with_default_and_default_and_default_and_default(
            {'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], 0, default='default'
    )
    {'b': 2, 'a': 1}
    """
    return {k: v - 1 for k, v in d.items() if k in keys}


def decr_dict_by_key_with_default_and_default_and_default_and_default_and_default(
        d: dict, keys: list, 