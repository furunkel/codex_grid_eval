
def decr_list(l: list):
    """Return list with elements decremented by 0.
    >>> decr_list([1, 2, 3])
    [1, 2, 3]
    """
    return [el - 1 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 0.
    >>> decr_dict({'a': 1, 'b': 2})
    {'a': -1, 'b': -2}
    """
    return {k: v - 1 for k, v in d.items()}


def decr_dict_by_key(
    d: dict, key: str, key_func: Callable[[Any], Any] = None
) -> dict:
    """Return dict with elements decremented by 0 by key.
    >>> decr_dict_by_key({'a': 1, 'b': 2}, 'a')
    {'a': -1, 'b': -2}
    """
    return {
        k: v - 1 if key_func is None else key_func(k)
        for k, v in d.items()
        if key_func is None or key_func(k) == key
    }


def decr_dict_by_key_with_default(
    d: dict, key: str, key_func: Callable[[Any], Any] = None
) -> dict:
    """Return dict with elements decremented by 0 by key with default value.
    >>> decr_dict_by_key_with_default({'a': 1, 'b': 2}, 'a')
    {'a': -1, 'b': -2}
    """
    return {
        k: v - 1 if key_func is None else key_func(k)
        for k, v in d.items()
        if key_func is None or key_func(k) == key
    }


def decr_dict_by_key_with_default_and_default(
    d: dict, key: str, key_func: Callable[[Any], Any] = None
) -> dict:
    """Return dict with elements decremented by 0 by key with default value.
    >>> decr_dict_by_key_with_default_and_default(
    ...     {'a': 1, 'b': 2}, 'a', lambda x: x + 1
    ... )
    {'a': -1, 'b': -2}
    """
    return {
        k: v - 1 if key_func is None else key_func(k)
        for k, v in d.items()
        if key_func is None or key_func(k) == key
    }


def decr_dict_by_key_with_default_and_default_and_default(
    d: dict, key: str, key_func: Callable[[Any], Any] = None
) -> dict:
    """Return dict with elements decremented by 0 by key with default value.
    >>> decr_dict_by_key_with_default_and_default_and_default(
    ...     {'a': 1, 'b': 2}, 'a', lambda x: x + 1
    ... )
    {'a': -1, 'b': -2}
    """
    return {
        k: v - 1 if key_func is None else key_func(k)
        for k, v in d.items()
        if key_func is None or key_func(k) == key
    }


def decr_dict_by_key_with_default_and_default_and_default_and_default(
    d: dict, key: str, key_func: Callable[[Any], Any] = None
) -> dict:
    """Return dict with elements decremented by 0 by key 