
def quadruples_sum_to_one(l: list):
    """
    quadruples_sum_to_one takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quadruples_sum_to_one([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 4 == 0:
        return True
    else:
        return False


def quadruples_sum_to_one_2(l: list):
    """
    quadruples_sum_to_one_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quadruples_sum_to_one_2([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 4 == 0:
        return True
    else:
        return False


def quadruples_sum_to_one_3(l: list):
    """
    quadruples_sum_to_one_3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quadruples_sum_to_one_3([1, 2, -3, 7, 2, 7])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 4 == 0:
        return True
    else:
        return False


def quadruples_sum_to_one_4(l: list):
    """
    quadruples_sum_to_one_4 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to one, and False otherwise.

    >>> quadr