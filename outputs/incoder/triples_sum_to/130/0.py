
def quadruples_sum_to_hundred(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum > 100:
            return True
        i += 1
    return False


def quadruples_sum_to_hundred_2(l: list):
    """
    quadruples_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_2([1, 2, -3, 7, 2, 7])
    False
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum > 100:
            return True
        i += 1
    return False


def quadruples_sum_to_hundred_3(l: list):
    """
    quadruples_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_3([1, 2, -3, 7, 2, 7])
    True
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l) - 1:
        sum += l[i]
        if sum > 100:
            return True
        i += 1
    return False


def quadruples_sum