
def doubles_sum_to_five(l: list):
    """
    doubles_sum_to_five takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five([1, 2, -3, 7, 2, 7])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 5:
            return True
    return False


def doubles_sum_to_five_iterative(l: list):
    """
    doubles_sum_to_five_iterative takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_iterative([1, 2, -3, 7, 2, 7])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 5:
            return True
    return False


def doubles_sum_to_five_memo(l: list):
    """
    doubles_sum_to_five_memo takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to five, and False otherwise.

    >>> doubles_sum_to_five_memo([1, 2, -3, 7, 2, 7])
    False
    """
    memo = {}
    for i in l:
        memo[i] = False
    for i in l:
        s += i
        if s in memo:
            memo[s] = True
    return memo


def doubles_sum_to_five_memo_iterative(l: list):
    """
    doubles_sum_to_five_memo_iterative takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list 