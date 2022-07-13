
def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 3:
            return True
    return False


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
        if sum == 5:
            return True
    return False


def doubles_sum_to_seven(l: list):
    """
    doubles_sum_to_seven takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to seven, and False otherwise.

    >>> doubles_sum_to_seven([1])
    False
    """
    sum = 0
    for i in l:
        sum += i
        if sum == 7:
            return True
    return False


def doubles_sum_to_nine(l: list):
    """
    doubles_sum_to_nine takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to nine, and False otherwise.

    >>> doubles_sum_to_nine([1])
    False
    """
    sum = 0
    for i in l:
