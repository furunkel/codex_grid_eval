
def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([1, 2, 3])
    [0, 1, 2]
    """
    return [x - 1 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 1, 'b': 2})
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict,
    key_func: Callable[[Any], Any],
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by key function.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, lambda k: k[0], lambda k: k[1])
    {'a': 2, 'b': 1}
    """
    return {
        key_func(k): value_func(v)
        for k, v in d.items()
    }


def decr_dict_by_values(
    d: dict,
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by value function.
    >>> decr_dict_by_values({'a': 1, 'b': 2}, lambda v: v[0])
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict,
    key_func: Callable[[Any], Any],
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by key function.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, lambda k: k[0], lambda k: k[1])
    {'a': 2, 'b': 1}
    """
    return {
        key_func(k): value_func(v)
        for k, v in d.items()
    }


def decr_dict_by_values(
    d: dict,
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by value function.
    >>> decr_dict_by_values({'a': 1, 'b': 2}, lambda v: v[0])
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict,
    key_func: Callable[[Any], Any],
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by key function.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, lambda k: k[0], lambda k: k[1])
    {'a': 2, 'b': 1}
    """
    return {
        key_func(k): value_func(v)
        for k, v in d.items()
    }


def decr_dict_by_values(
    d: dict,
    value_func: Callable[[Any], Any],
):
    """Return dict with elements decremented by 1 by value function.
    >>> decr_dict_by_