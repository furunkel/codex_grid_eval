
def decuples_sum_to_hundred(l: list):
    """
    decuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 10 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> decuples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    s = 0
    for x in l:
        s += x
        if s == 100:
            return True
    return False


def decuples_sum_to_hundred_list(l: list):
    """
    decuples_sum_to_hundred_list takes a list of integers as an input.
    it returns a list of integers that sum to hundred.

    >>> decuples_sum_to_hundred_list([1, 2, -3, 7, 2, 7])
    [1, 3, 7]
    """
    s = 0
    lst = []
    for x in l:
        s += x
        if s == 100:
            lst.append(x)
    return lst


def decuples_sum_to_hundred_list_with_duplicates(l: list):
    """
    decuples_sum_to_hundred_list_with_duplicates takes a list of integers as an input.
    it returns a list of integers that sum to hundred, and a list of duplicates.

    >>> decuples_sum_to_hundred_list_with_duplicates([1, 2, -3, 7, 2, 7])
    [1, 3, 7, [2, 7]]
    """
    s = 0
    lst = []
    lst2 = []
    for x in l:
        s += x
        if s == 100:
            lst.append(x)
            lst2.append(x)
    return lst, lst2


def decuples_sum_to_hundred_list_with_duplicates_2(l: list):
    """
    decuples_sum_to_