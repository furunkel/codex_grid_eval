def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1])
    False
    """
    return len(l) == 2 and sum(l) % 2 == 0


def doubles_sum_to_ten(l: list):
    """
    doubles_sum_to_ten takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to ten, and False otherwise.

    >>> doubles_sum_to_ten([1, 2, 3])
    True
    """
    return len(l) == 3 and sum(l) % 3 == 0


def doubles_sum_to_twenty(l: list):
    """
    doubles_sum_to_twenty takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to twenty, and False otherwise.

    >>> doubles_sum_to_twenty([1, 2, 3])
    True
    """
    return len(l) == 4 and sum(l) % 4 == 0


def doubles_sum_to_thirty(l: list):
    """
    doubles_sum_to_thirty takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to thirty, and False otherwise.

    >>> doubles_sum_to_thirty([1, 2, 3])
    True
    """
    return len(l) == 5 and sum(l) % 5 == 0


def doubles_sum_to_fourteen(l: list):
    """
    doubles_sum_to_fourteen takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to fourteen, and False otherwise.

    >>> doubles_sum_to_fourteen([1, 2, 3])
    True
    """
    return len(l) == 6 and sum(l) % 6 == 0


def doubles_sum_to_fifteen(