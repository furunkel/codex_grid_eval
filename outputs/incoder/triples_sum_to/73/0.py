
def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 3:
            return True
    return False


@numba.jit(nopython=True)
def doubles_sum_to_four(l: list):
    """
    doubles_sum_to_four takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to four, and False otherwise.

    >>> doubles_sum_to_four([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 4:
            return True
    return False


@numba.jit(nopython=True)
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 3, -2, 1, 5, 8])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 5:
            return True
    return False


@numba.jit(nopython=True)
def doubles_sum_to_six(l: list):
    """
    doubles_sum_to_six takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to si