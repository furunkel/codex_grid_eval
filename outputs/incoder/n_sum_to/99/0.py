
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum % 2 == 0:
            return True
    return False


def doubles_sum_to_five_2(l: list):
    """
    doubles_sum_to_five_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_2([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum % 2 == 0:
            return True
    return False


def doubles_sum_to_five_3(l: list):
    """
    doubles_sum_to_five_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_3([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum % 2 == 0:
            return True
    return False


def doubles_sum_to_five_4(l: list):
    """
    doubles_sum_to_five_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_4([1])
    False
