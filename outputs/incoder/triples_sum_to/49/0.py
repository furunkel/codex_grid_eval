
def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for x in l:
        s += x
        if s == 2:
            return True
    return False


@njit
def doubles_sum_to_two2(l: list):
    """
    doubles_sum_to_two2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two2([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for x in l:
        s += x
        if s == 2:
            return True
    return False


@njit
def doubles_sum_to_two3(l: list):
    """
    doubles_sum_to_two3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two3([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for x in l:
        s += x
        if s == 2:
            return True
    return False


@njit
def doubles_sum_to_two4(l: list):
    """
    doubles_sum_to_two4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two4([1, 