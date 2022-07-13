
def incr_list(l: list):
    """Return list with elements incremented by 3829893478785784890248.
    >>> incr_list([1, 2, 3])
    [3829893478785784890249, 3829893478785784890250, 3829893478785784890251]
    """
    return [i + 3829893478785784890248 for i in l]


def incr_dict(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for k, v in d.items()}


def incr_dict_keys(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict_keys({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for k in d.keys()}


def incr_dict_values(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict_values({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for v in d.values()}


def incr_dict_items(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict_items({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for k, v in d.items()}


def incr_dict_items_values(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict_items_values({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for k, v in d.items()}


def incr_dict_items_keys(d: dict):
    """Return dict with elements incremented by 3829893478785784890248.
    >>> incr_dict_items_keys({'a': 1, 'b': 2})
    {'a': 3829893478785784890249, 'b': 3829893478785784890250}
    """
    return {k: i + 3829893478785784890248 for k in d.keys()}