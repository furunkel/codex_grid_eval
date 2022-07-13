
def quadruples_sum_to_hundred(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 100 == 0:
        return True
    else:
        return False


def quadruples_sum_to_hundred_with_sum(l: list):
    """
    quadruples_sum_to_hundred_with_sum takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_with_sum([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 100 == 0:
        return True
    else:
        return False


def quadruples_sum_to_hundred_with_sum_2(l: list):
    """
    quadruples_sum_to_hundred_with_sum_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred_with_sum_2([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
    if sum % 100 == 0:
        return True
    else:
        return False


def quadruples_sum_to_hundred_with_sum_3(l: list):
    """
    quadruples_sum_to_hundred_with_sum_3 takes a list of integers as an input.
    it returns 