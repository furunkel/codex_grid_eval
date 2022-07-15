
def quadruples_sum_to_zero(l: list):
    """
    quadruples_sum_to_zero takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero([1, 2, -3, 7, 2, 7])
    False
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum == 0:
            return True
        i += 1
    return False


def quadruples_sum_to_zero2(l: list):
    """
    quadruples_sum_to_zero2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero2([1, 2, -3, 7, 2, 7])
    True
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum == 0:
            return True
        i += 1
    return False


def quadruples_sum_to_zero3(l: list):
    """
    quadruples_sum_to_zero3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> quadruples_sum_to_zero3([1, 2, -3, 7, 2, 7])
    False
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum == 0:
            return True
        i += 1
    return False


def quadruples_sum_to_zero4(l: list):
    """
    quadr