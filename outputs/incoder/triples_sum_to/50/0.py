
def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 2:
            return True
    return False


@njit
def doubles_sum_to_two_inplace(l: list):
    """
    doubles_sum_to_two_inplace takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_inplace([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 2:
            return True
    return False


@njit
def doubles_sum_to_two_inplace_fast(l: list):
    """
    doubles_sum_to_two_inplace_fast takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_inplace_fast([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 2:
            return True
    return False


@njit
def doubles_sum_to_two_inplace_slow(l: list):
    """
    doubles_sum_to_two_inplace_slow takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and 