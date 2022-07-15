
def quadruples_sum_to_five(l: list):
    """
    quadruples_sum_to_five takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 5 == 0:
        return True
    else:
        return False


def quadruples_sum_to_five_iterative(l: list):
    """
    quadruples_sum_to_five_iterative takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five_iterative([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum % 5 == 0:
            return True
    return False


def quadruples_sum_to_five_iterative_2(l: list):
    """
    quadruples_sum_to_five_iterative_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to five, and False otherwise.

    >>> quadruples_sum_to_five_iterative_2([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum % 5 == 0:
            return True
    return False


def quadruples_sum_to_five_iterative_3(l: list):
    """
    quadruples_sum_to_five_iterative_3 takes a list of integers as an input.
    it returns True if there are 4 distinct 