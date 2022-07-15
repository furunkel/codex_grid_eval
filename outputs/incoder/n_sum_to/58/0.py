
def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    l = sorted(l)
    sum = 0
    count = 0
    for x in l:
        sum += x
        if sum == 2:
            count += 1
            if count == 4:
                return True
    return False


def quadruples_sum_to_two2(l: list):
    """
    quadruples_sum_to_two2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two2([1, 2, -3, 7, 2, 7])
    True
    """
    l = sorted(l)
    sum = 0
    count = 0
    for x in l:
        sum += x
        if sum == 2:
            count += 1
            if count == 4:
                return True
    return False


def quadruples_sum_to_two3(l: list):
    """
    quadruples_sum_to_two3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two3([1, 2, -3, 7, 2, 7])
    True
    """
    l = sorted(l)
    sum = 0
    count = 0
    for x in l:
        sum += x
        if sum == 2:
            count += 1
            if count == 4:
                return True
    return False


def quadruples_sum_to_two4(l: list):
    """
    quadruple