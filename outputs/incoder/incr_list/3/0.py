
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    l = list(l)
    l.sort()
    l.insert(0, 0)
    l[len(l) - 1] += 1
    return l


def incr_dict(d: dict):
    """Return dict with elements incremented by 1.
    >>> incr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 1, 'b': 3, 'c': 4}
    """
    d = dict(d)
    for k, v in d.items():
        d[k] += 1
    return d


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 2, 'b': 1, 'c': 0}
    """
    d = dict(d)
    for k, v in d.items():
        d[k] -= 1
    return d


def decr_dict_by_key(
    d: dict, key: Callable[[Any], Any]
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3}, lambda x: x % 2)
    {'a': 2, 'b': 1, 'c': 0}
    """
    d = dict(d)
    for k, v in d.items():
        d[k] = d[key(v)] - 1
    return d


def decr_list(l: list):
    """Return list with elements decremented by 1.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 123]
    """
    l = list(l)
    l.sort()
    l.reverse()
    l[len(l) - 1] -= 1
    return l


def decr_dict(d: dict):
    """Return dict with elements decremented by 1.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': 2, 'b': 1, 'c': 0}
    """
    d = dict(d)
    for k, v in d.items():
        d[k] = d[k] - 1
    return d


def decr_dict_by_key(
    d: dict, key: Callable[[Any], Any]
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_dict_by_key({'a': 1, 'b': 2, 'c': 3}, lambda x: x % 2)
    {'a': 2, 'b': 1, 'c': 0}
    """
    d = dict(d)
    for k, v in d.items():
        d[k] = d[key(v)] - 1
    return d


def decr_list_by_key(
    l: list, key: Callable[[Any], Any]
) -> Dict[Any, Any]:
    """Return dict with elements decremented by 1 by key.
    >>> decr_list_by_key([5, 3, 5, 2, 3, 3, 9, 0, 123], lambda x: x % 2)
    {'a': 2, 'b': 1, 'c': 0}
    """
    l = list(l)
    l.sort()
    l.reverse()
