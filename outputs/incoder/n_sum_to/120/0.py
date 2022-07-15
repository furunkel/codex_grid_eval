
def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            return True
    return False


def doubles_sum_to_hundred_2(l: list):
    """
    doubles_sum_to_hundred_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_2([1, 3, 5, 0])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            return True
    return False


def doubles_sum_to_hundred_3(l: list):
    """
    doubles_sum_to_hundred_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_3([1, 3, 5, 0])
    True
    """
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            return True
    return False


def doubles_sum_to_hundred_4(l: list):
    """
    doubles_sum_to_hundred_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_4([1, 3, 5, 0])
    True