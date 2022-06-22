
def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 100:
                return True
    return False


def doubles_sum_to_hundred_v2(l: list):
    """
    doubles_sum_to_hundred_v2 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_v2([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 100:
                return True
    return False


def doubles_sum_to_hundred_v3(l: list):
    """
    doubles_sum_to_hundred_v3 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_v3([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 100:
                return True
    return False


def doubles_sum_to_hundred_v4(l: list):
    """
    doubles_sum_to_hundred_v4 takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_v4([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 100:
                return True
    return False


def doubles_sum_to_hundred_v5(l: list):
    """
    doubles_sum_to_hundred