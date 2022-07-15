
def decuples_sum_to_three(l: list):
    """
    decuples_sum_to_three takes a list of integers as an input.
    it returns True if there are 10 distinct elements in the list that
    sum to three, and False otherwise.

    >>> decuples_sum_to_three([1, 3, 5, 0])
    False
    """
    s = 0
    for x in l:
        s += x
        if s == 3:
            return True
    return False


def decuples_sum_to_five(l: list):
    """
    decuples_sum_to_five takes a list of integers as an input.
    it returns True if there are 10 distinct elements in the list that
    sum to five, and False otherwise.

    >>> decuples_sum_to_five([1, 3, 5, 0])
    True
    """
    s = 0
    for x in l:
        s += x
        if s == 5:
            return True
    return False


def decuples_sum_to_ten(l: list):
    """
    decuples_sum_to_ten takes a list of integers as an input.
    it returns True if there are 10 distinct elements in the list that
    sum to ten, and False otherwise.

    >>> decuples_sum_to_ten([1, 3, 5, 0])
    True
    """
    s = 0
    for x in l:
        s += x
        if s == 10:
            return True
    return False


def decuples_sum_to_eleven(l: list):
    """
    decuples_sum_to_eleven takes a list of integers as an input.
    it returns True if there are 10 distinct elements in the list that
    sum to eleven, and False otherwise.

    >>> decuples_sum_to_eleven([1, 3, 5, 0])
    True
    """
    s = 0
    for 