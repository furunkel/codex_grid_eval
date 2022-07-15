
def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1, 2, -3, 7, 2, 7])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 2:
            return True
    return False


def doubles_sum_to_one_2(l: list):
    """
    doubles_sum_to_one_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_2([1, 2, -3, 7, 2, 7])
    True
    """
    s = 0
    for i in l:
        s += i
        if s == 2:
            return True
    return False


def doubles_sum_to_one_3(l: list):
    """
    doubles_sum_to_one_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_3([1, 2, -3, 7, 2, 7])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 2:
            return True
    return False


def doubles_sum_to_one_4(l: list):
    """
    doubles_sum_to_one_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one_4([1, 2, -3, 7, 2, 7])
    True
    """
    s = 0
    for i in l:
        s += i