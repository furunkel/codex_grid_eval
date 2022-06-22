
def decr_list(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return [x - 100 for x in l]


def decr_list_map(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return list(map(lambda x: x - 100, l))


def decr_list_map_lambda(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list_map_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return list(map(lambda x: x - 100, l))


def decr_list_map_lambda_lambda(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list_map_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return list(map(lambda x: x - 100, l))


def decr_list_map_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list_map_lambda_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [-95, -97, -95, -98, -97, -97, -91, -100, 23]
    """
    return list(map(lambda x: x - 100, l))


def decr_list_map_lambda_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 100.
    >>> decr_list_map_lambda_lambda_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
   