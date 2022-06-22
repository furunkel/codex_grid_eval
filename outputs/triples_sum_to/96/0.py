
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 5:
                return True
    return False


def doubles_sum_to_five_v2(l: list):
    """
    doubles_sum_to_five_v2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_v2([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        if 5 - l[i] in l[i + 1:]:
            return True
    return False


def doubles_sum_to_five_v3(l: list):
    """
    doubles_sum_to_five_v3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_v3([1, 3, 5, 0])
    True
    """
    return any(5 - x in l[i + 1:] for i, x in enumerate(l))


def doubles_sum_to_five_v4(l: list):
    """
    doubles_sum_to_five_v4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_v4([1, 3, 5, 0])
    True
    """
    return any(5 - x in l[i + 1:] for i, x in enumerate(l))


def doubles_sum_to_five_v5(l: list):
    """
    doubles_sum_to_five_v5 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_v5([1, 3, 5, 0])