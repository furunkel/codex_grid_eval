
def doubles_sum_to_three(l: list):
    """
    doubles_sum_to_three takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 3:
                return True
    return False


def doubles_sum_to_three_v2(l: list):
    """
    doubles_sum_to_three_v2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three_v2([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        if 3 - l[i] in l[i + 1:]:
            return True
    return False


def doubles_sum_to_three_v3(l: list):
    """
    doubles_sum_to_three_v3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three_v3([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        if 3 - l[i] in l[:i] + l[i + 1:]:
            return True
    return False


def doubles_sum_to_three_v4(l: list):
    """
    doubles_sum_to_three_v4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to three, and False otherwise.

    >>> doubles_sum_to_three_v4([1, 3, 5, 0])
    True
    """
    for i in range(len(l)):
        if 3 - l[i] in l[:i] or 3 - l[i] in l[i + 1:]:
            return True
    return False


def doubles_sum_to_three_v5(l: list):
    """
    doubles_sum_to_three_v5 takes a list of integers as an input.
    it returns