
def decr_list(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return [x - 9999 for x in l]


def decr_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict({'a': 1, 'b': 2, 'c': 3})
    {'a': -9998, 'b': -9997, 'c': -9996}
    """
    return {k: x - 9999 for k, v in d.items()}


def decr_dict_list(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list({'a': [1, 2, 3], 'b': [4, 5, 6]})
    {'a': [-9998, -9997, -9996], 'b': [-9998, -9997, -9996]}
    """
    return {k: decr_list(v) for k, v in d.items()}


def decr_dict_list_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list_dict({'a': [{'a': 1}, {'a': 2}], 'b': [{'b': 1}, {'b': 2}]})
    {'a': [{'a': -9998}, {'a': -9997}, {'a': -9996}], 'b': [{'b': -9998}, {'b': -9997}, {'b': -9996}]}
    """
    return {k: decr_dict(v) for k, v in d.items()}


def decr_dict_list_dict_list(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list_dict_list({'a': [{'a': [1, 2]}, {'a': [3, 4]}], 'b': [{'b': [1, 2]}, {'b': [3, 4]}]})
    {'a': [{'a': [-9998, -9997]}, {'a': [-9998, -9997]}], 'b': [{'b': [-9998, -9997]}, {'b': [-9998, -9997]}]}
    """
    return {k: decr_dict_list(v) for k, v in d.items()}


def decr_dict_list_dict_list_dict(d: dict):
    """Return dict with elements decremented by 9999.
    >>> decr_dict_list_dict_list_dict({'a': [{'a': [[1, 2]]}, {'a': [[3, 4]]}], 'b': [{'b': [[1, 2]]}, {'b': [[3, 4]]}]})
    {'a': [{'a': [[-9998, -9997]]}, {'a': [[-9998, -9997]]}], 'b': [{'b': [[-9998, -9997]]}, {'b': [[-9998, -9997]]}]}
    """
    return {k: decr_dict_list_dict(v) for k, v in d.items()}


def decr_dict_list_dict_list_dict_list(