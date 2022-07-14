def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 2, -3, 7, 2, 7])
    False
    """
    return len(l) == 2 and sum(l) % 2 == 0


def doubles_sum_to_ten(l: list):
    """
    doubles_sum_to_ten takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to ten, and False otherwise.

    >>> doubles_sum_to_ten([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) % 2 == 1


def doubles_sum_to_twenty(l: list):
    """
    doubles_sum_to_twenty takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to twenty, and False otherwise.

    >>> doubles_sum_to_twenty([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) % 2 == 0


def doubles_sum_to_thirty(l: list):
    """
    doubles_sum_to_thirty takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to thirty, and False otherwise.

    >>> doubles_sum_to_thirty([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and sum(l) % 2 == 1


def doubles_sum_to_fourteen(l: list):
    """
    doubles_sum_to_fourteen takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to fourteen, and False otherwise.

    >>> doubles_sum_to_fourteen([1, 2, -3, 7