
def incr_list(l: list):
    """Return list with elements incremented by 2.
    >>> incr_list([1, 2, 3])
    [3, 4, 5]
    """
    return [x + 2 for x in l]


@njit
def incr_dict(d: dict):
    """Return dict with elements incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k: v + 2 for k, v in d.items()}


@njit
def incr_dict_keys(d: dict):
    """Return dict with keys incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_values(d: dict):
    """Return dict with values incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k: v + 2 for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def incr_dict_items(d: dict):
    """Return dict with items incremented by 2.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3, 'b': 4}
    """
    return {k + 2: v for k, v in d.items()}


@njit
def in