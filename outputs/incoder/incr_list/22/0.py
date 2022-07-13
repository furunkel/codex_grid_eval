
def decr_list(l: list):
    """Return list with elements decremented by 3829893478785784890248.
    >>> decr_list([1, 2, 3])
    [-3829893478785784890247, -3829893478785784890246, -3829893478785784890245]
    """
    return [x - 3829893478785784890248 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 3829893478785784890248.
    >>> decr_dict({1: 2, 3: 4})
    {1: -3829893478785784890247, 3: -3829893478785784890246}
    """
    return {x: x - 3829893478785784890248 for x in d.keys()}


def decr_dict_list(d: dict):
    """Return dict with elements decremented by 3829893478785784890248.
    >>> decr_dict_list([{1: 2, 3: 4}, {5: 6, 7: 8}])
    [{1: -3829893478785784890247, 3: -3829893478785784890246}, {5: -3829893478785784890248, 7: -3829893478785784890249}]
    """
    return [{x: x - 3829893478785784890248 for x in d.keys()}]


def decr_dict_list_dict(d: dict):
    """Return dict with elements decremented by 3829893478785784890248.
    >>> decr_dict_list_dict([{1: 2, 3: 4}, {5: 6, 7: 8}])
    [{1: -3829893478785784890247, 3: -3829893478785784890246}, {5: -3829893478785784890248, 7: -3829893478785784890249}]
    """
    return [{x: x - 3829893478785784890248 for x in d.keys()}]


def decr_dict_list_dict_list(d: dict):
    """Return dict with elements decremented by 3829893478785784890248.
    >>> decr_dict_list_dict_list([{1: 2, 3: 4}, {5: 6, 7: 8}])
    [{1: -3829893478785784890247, 3: -3829893478785784890246}, {5: -3829893478785784890248, 7: -3829893478785784890249}]
    """
    return [{x: x - 3829893478785784890248 for x in d.keys()}]


def decr_dict_list_dict_list_dict(d: dict):
    """Return dict with elements decremented by 3829893478785784890248.
    >>> decr_dict_list_dict_list_dict([{1: 2, 3: 4}, {5: 6, 7