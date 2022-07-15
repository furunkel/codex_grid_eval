
def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1, 3, 5, 0])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 1:
            return False
    return True


def doubles_sum_to_one_2(l: list):
    """
    doubles_sum_to_one_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_2([1, 3, 5, 0])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 1:
            return False
    return True


def doubles_sum_to_one_3(l: list):
    """
    doubles_sum_to_one_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_3([1, 3, 5, 0])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 1:
            return False
    return True


def doubles_sum_to_one_4(l: list):
    """
    doubles_sum_to_one_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_4([1, 3, 5, 0])
    True
    """
    sum = 0
    for i in l:
        sum += i