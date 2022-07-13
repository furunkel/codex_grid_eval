
def quadruples_sum_to_hundred(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            return True
    return False


def quadruples_sum_to_hundred_list(l: list):
    """
    quadruples_sum_to_hundred_list takes a list of integers as an input.
    it returns a list of quadruples that sum to hundred.

    >>> quadruples_sum_to_hundred_list([1,2])
    [(1, 2), (2, 1)]
    """
    quadruples = []
    for i in l:
        quadruples.append((i, i))
    return quadruples


def quadruples_sum_to_hundred_list_2(l: list):
    """
    quadruples_sum_to_hundred_list_2 takes a list of integers as an input.
    it returns a list of quadruples that sum to hundred.

    >>> quadruples_sum_to_hundred_list_2([1,2])
    [(1, 2), (2, 1)]
    """
    quadruples = []
    for i in l:
        quadruples.append((i, i))
    return quadruples


def quadruples_sum_to_hundred_list_3(l: list):
    """
    quadruples_sum_to_hundred_list_3 takes a list of integers as an input.
    it returns a list of quadruples that sum to hundred.

    >>> quadruples_sum_to_hundred_list_3([1,2])
    [(1, 2), (2, 1)]
