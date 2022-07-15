
def doubles_sum_to_one(l: list):
    """
    doubles_sum_to_one takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one([1])
    False
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l):
        sum += l[i]
        if sum > 1:
            return True
        i += 1
    return False


def doubles_sum_to_one2(l: list):
    """
    doubles_sum_to_one2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one2([1,2])
    True
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l):
        sum += l[i]
        if sum > 1:
            return True
        i += 1
    return False


def doubles_sum_to_one3(l: list):
    """
    doubles_sum_to_one3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to one, and False otherwise.

    >>> doubles_sum_to_one3([1,2])
    True
    """
    l = sorted(l)
    sum = 0
    i = 0
    while i < len(l):
        sum += l[i]
        if sum > 1:
            return True
        i += 1
    return False


def doubles_sum_to_one4(l: list):
    """
    doubles_sum_to_one4 takes a list of integers as an input.
