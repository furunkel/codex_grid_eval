
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 2, -3, 7, 2, 7])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 5:
                return True
    return False


def doubles_sum_to_five_set(l: list):
    """
    doubles_sum_to_five_set takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_set([1, 2, -3, 7, 2, 7])
    False
    """
    s = set(l)
    for i in s:
        if 5 - i in s:
            return True
    return False


def doubles_sum_to_five_set_2(l: list):
    """
    doubles_sum_to_five_set_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_set_2([1, 2, -3, 7, 2, 7])
    False
    """
    s = set(l)
    return any(5 - i in s for i in s)


def doubles_sum_to_five_set_3(l: list):
    """
    doubles_sum_to_five_set_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_set_3([1, 2, -3, 7, 2, 7])
    False
    """
    s = set(l)
    return len(s) != len(l) and any(5 - i in s for i in s)


def doubles_sum_to_five_set_4(l: list):
    """
    doubles_sum_to_five_set_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

