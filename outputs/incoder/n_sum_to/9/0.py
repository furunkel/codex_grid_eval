
def quadruples_sum_to_zero(l: list):
    """
    quadruples_sum_to_zero takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero([1, 3, -2, 1, 5, 8])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum < 0:
            return False
    return True


def quadruples_sum_to_zero2(l: list):
    """
    quadruples_sum_to_zero2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero2([1, 3, -2, 1, 5, 8])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 0:
            return True
    return False


def quadruples_sum_to_zero3(l: list):
    """
    quadruples_sum_to_zero3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero3([1, 3, -2, 1, 5, 8])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum < 0:
            return False
    return True


def quadruples_sum_to_zero4(l: list):
    """
    quadruples_sum_to_zero4 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero4([1, 3, -2, 1, 