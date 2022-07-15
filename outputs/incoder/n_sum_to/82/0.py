
def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for x in l:
        sum += x
        if sum > 3:
            return False
    return True


def quadruples_sum_to_four(l: list):
    """
    quadruples_sum_to_four takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to four, and False otherwise.

    >>> quadruples_sum_to_four([1, 2, -3, 7, 2, 7])
    True
    """
    sum = 0
    for x in l:
        sum += x
        if sum > 4:
            return False
    return True


def quadruples_sum_to_five(l: list):
    """
    quadruples_sum_to_five takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five([1, 2, -3, 7, 2, 7])
    True
    """
    sum = 0
    for x in l:
        sum += x
        if sum > 5:
            return False
    return True


def quadruples_sum_to_six(l: list):
    """
    quadruples_sum_to_six takes a list of integers as an input.
    it returns True if there are 7 distinct elements in the list that
    sum to six, and False otherwise.

    >>> quadruples_sum_to_six([1, 2, -3, 7, 2, 7])