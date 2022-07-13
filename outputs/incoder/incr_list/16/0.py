
def decr_list(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list([1, 2, 3])
    [-1, 0, 1]
    """
    return [el - 2 for el in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 2.
    >>> decr_dict({1: 2, 3: 4})
    {1: 0, 3: 2}
    """
    return {el - 2: el for el in d.values()}


def decr_dict_by_key(
    d: dict, key: Callable[[Any], Any]
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 2 by key.
    >>> decr_dict_by_key({1: 2, 3: 4}, lambda x: x // 2)
    {1: 0, 3: 2}
    """
    return {
        el - 2: {key: el for el in d.values()}[key](key)
        for key in d.keys()
    }


def decr_dict_by_key_values(
    d: dict, key: Callable[[Any], Any], values: Callable[[Any], Any]
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 2 by key and values.
    >>> decr_dict_by_key_values(
    ...     {1: 2, 3: 4},
    ...     lambda x: x // 2,
    ...     lambda x: x % 2,
    ... )
    {1: 0, 3: 2}
    """
    return {
        el - 2: {key: el for el in d.values()}[key](key)
        for key in d.keys()
    }


def decr_dict_by_key_values_list(
    d: dict, key: Callable[[Any], Any], values: Callable[[Any], Any], l: list
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 2 by key and values and list.
    >>> decr_dict_by_key_values_list(
    ...     {1: 2, 3: 4},
    ...     lambda x: x // 2,
    ...     lambda x: x % 2,
    ...     [1, 2, 3],
    ... )
    {1: 0, 3: 2}
    """
    return {
        el - 2: {key: el for el in d.values()}[key](key)
        for key in d.keys()
    }


def decr_dict_by_key_values_dict(
    d: dict, key: Callable[[Any], Any], values: Callable[[Any], Any], d: dict
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 2 by key and values and dict.
    >>> decr_dict_by_key_values_dict(
    ...     {1: 2, 3: 4},
    ...     lambda x: x // 2,
    ...     lambda x: x % 2,
    ...     {1: 2, 3: 4},
    ... )
    {1: 0, 3: 2}
    """
    return {
        el - 2: {key: el for el in d.values()}[key](key)
        for key in d.keys()
    }


def decr_dict_by_key_values_dict_list(
    d: dict, key: Callable[[Any], Any], values: Callable[[