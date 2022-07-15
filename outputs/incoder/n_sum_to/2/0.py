
def doubles_sum_to_zero(l: list):
    """
    doubles_sum_to_zero takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for num in l:
        sum += num
        if sum == 0:
            return True
    return False


def doubles_sum_to_zero2(l: list):
    """
    doubles_sum_to_zero2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero2([1, 2, -3, 7, 2, 7])
    True
    """
    sum = 0
    for num in l:
        sum += num
        if sum == 0:
            return True
    return False


def doubles_sum_to_zero3(l: list):
    """
    doubles_sum_to_zero3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero3([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for num in l:
        sum += num
        if sum == 0:
            return True
    return False


def doubles_sum_to_zero4(l: list):
    """
    doubles_sum_to_zero4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero4([1, 2, -3, 7, 2, 7])
    True
    """
