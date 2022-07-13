
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    """
    return l + [el + 1] for el in l


def incr_dict(d: dict):
    """Return dict with elements incremented by 1.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 1, 'b': 3, 'c': 2}
    """
    return {k: v + 1 for k, v in d.items()}


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 1, 'b': 2})
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([1, 2, 3])
    [1, 2, 2]
    """
    return [el - 1 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 1, 'b': 2})
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: Callable[[dict], Any]
) -> Union[dict, list]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, lambda x: x['b'])
    {'a': 2, 'b': 1}
    """
    return {k: v - 1 for k, v in d.items() if key(d) == k}


def decr_list_by_key(
    l: list, key: Callable[[dict], Any]
) -> Union[dict, list]:
    """Return list with elements decremented by 1 by key.
    >>> decr_list_by_key([1, 2, 3], lambda x: x['b'])
    [1, 2, 2]
    """
    return [el - 1 for el in l if key(l) == el]


def decr_dict_by_key_with_default(
    d: dict, key: Callable[[dict], Any], default: Any
) -> Union[dict, list]:
    """Return dict with elements decremented by 1 by key and default value.
    >>> decr_dict_by_key_with_default(
    ...     {'a': 1, 'b': 2}, lambda x: x['b'], 0
    ... )
    {'a': 2, 'b': 1}
    """
    return {
        k: v - 1 if key(d) == k else default
        for k, v in d.items()
    }


def decr_list_by_key_with_default(
    l: list, key: Callable[[dict], Any], default: Any
) -> Union[dict, list]:
    """Return list with elements decremented by 1 by key and default value.
    >>> decr_list_by_key_with_default(
    ...     [1, 2, 3], lambda x: x['b'], 0
    ... )
    [1, 2, 2]
    """
    return [el - 1 if key(l) == el else default for el in l if key(l) == 