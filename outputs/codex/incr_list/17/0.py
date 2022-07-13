
def decr_list(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return [x - 2 for x in l]


def decr_list_map(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list_map([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return list(map(lambda x: x - 2, l))


def decr_list_map_lambda(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list_map_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return list(map(lambda x: x - 2, l))


def decr_list_map_lambda_lambda(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list_map_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return list(map(lambda x: x - 2, l))


def decr_list_map_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list_map_lambda_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
    return list(map(lambda x: x - 2, l))


def decr_list_map_lambda_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 2.
    >>> decr_list_map_lambda_lambda_lambda_lambda([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [3, 1, 3, 0, 1, 1, 7, -2, 121]
    """
