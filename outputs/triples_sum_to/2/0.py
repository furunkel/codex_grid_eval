
def doubles_sum_to_zero(l: list):
    """
    doubles_sum_to_zero takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero([1, 2, -3, 7, 2, 7])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False


def doubles_sum_to_zero_set(l: list):
    """
    doubles_sum_to_zero_set takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero_set([1, 2, -3, 7, 2, 7])
    False
    """
    s = set()
    for i in l:
        if -i in s:
            return True
        s.add(i)
    return False


def doubles_sum_to_zero_set_2(l: list):
    """
    doubles_sum_to_zero_set_2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero_set_2([1, 2, -3, 7, 2, 7])
    False
    """
    s = set(l)
    for i in l:
        if -i in s:
            return True
    return False


def doubles_sum_to_zero_set_3(l: list):
    """
    doubles_sum_to_zero_set_3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> doubles_sum_to_zero_set_3([1, 2, -3, 7, 2, 7])
    False
    """
    s = set(l)
    return any(-i in s for i in l)


def doubles_sum_to_zero_set_4(l: list):
    """
    doubles_sum_to_zero_set_4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to zero, and False otherwise.