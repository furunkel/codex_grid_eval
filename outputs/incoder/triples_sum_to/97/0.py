
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 3, -2, 1, 5, 8])
    False
    """
    doubles = 0
    sum = 0
    for x in l:
        sum += x
        if sum > 5:
            doubles += 1
            if doubles == 2:
                return True
    return False


def doubles_sum_to_five_with_comprehension(l: list):
    """
    doubles_sum_to_five_with_comprehension takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_with_comprehension([1, 3, -2, 1, 5, 8])
    False
    """
    return len([x for x in l if x > 5 and sum(x) == 5]) == 2


def doubles_sum_to_five_with_comprehension_2(l: list):
    """
    doubles_sum_to_five_with_comprehension_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_with_comprehension_2([1, 3, -2, 1, 5, 8])
    False
    """
    return len([x for x in l if x > 5 and sum(x) == 5]) == 2


def doubles_sum_to_five_with_comprehension_3(l: list):
    """
    doubles_sum_to_five_with_comprehension_3 takes a list of 