def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0])


def doubles_sum_to_hundred_with_one_element(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_one_element([1, 3, -2, 1, 5, 8])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and len(l[1]) == 1


def doubles_sum_to_hundred_with_two_elements(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_two_elements([1, 3, -2, 1, 5, 8])
    True
    """
    if len(l) == 0:
        return False
    return sum(l) == len(l[0]) and len(l[1]) == 2


def doubles_sum_to_hundred_with_three_elements(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_three_elements([1, 3, -2, 1, 5, 8])
    True
    """
    if len(l