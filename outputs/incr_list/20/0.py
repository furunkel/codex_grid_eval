
def decr_list(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return [x - 9999 for x in l]


def decr_list_map(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return list(map(lambda x: x - 9999, l))


def decr_list_map_lambda(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map_lambda([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return list(map(lambda x: x - 9999, l))


def decr_list_map_lambda_lambda(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map_lambda_lambda([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return list(map(lambda x: x - 9999, l))


def decr_list_map_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map_lambda_lambda_lambda([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return list(map(lambda x: x - 9999, l))


def decr_list_map_lambda_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map_lambda_lambda_lambda_lambda([1, 2, 3])
    [-9998, -9997, -9996]
    """
    return list(map(lambda x: x - 9999, l))


def decr_list_map_lambda_lambda_lambda_lambda_lambda(l: list):
    """Return list with elements decremented by 9999.
    >>> decr_list_map_lambda_lambda_lambda_lambda_lambda([1, 2, 3])
    [-9998, -9997, -