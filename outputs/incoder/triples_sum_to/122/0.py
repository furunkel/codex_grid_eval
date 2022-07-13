
def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    total = 0
    for num in l:
        total += num
        if total >= 100:
            return True
    return False


def doubles_sum_to_hundred_2(l: list):
    """
    doubles_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_2([1, 2, -3, 7, 2, 7])
    True
    """
    total = 0
    for num in l:
        total += num
        if total >= 100:
            return True
    return False


def doubles_sum_to_hundred_3(l: list):
    """
    doubles_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_3([1, 2, -3, 7, 2, 7])
    True
    """
    total = 0
    for num in l:
        total += num
        if total >= 100:
            return True
    return False


def doubles_sum_to_hundred_4(l: list):
    """
    doubles_sum_to_hundred_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> 