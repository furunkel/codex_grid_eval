
def triples_sum_to_five(l: list):
    """
    triples_sum_to_five takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five([1, 3, -2, 1, 5, 8])
    True
    """
    total = 0
    for num in l:
        total += num
        if total > 5:
            return True
    return False


def triples_sum_to_five_2(l: list):
    """
    triples_sum_to_five_2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five_2([1, 3, -2, 1, 5, 8])
    True
    """
    total = 0
    for num in l:
        total += num
        if total > 5:
            return True
    return False


def triples_sum_to_five_3(l: list):
    """
    triples_sum_to_five_3 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five_3([1, 3, -2, 1, 5, 8])
    True
    """
    total = 0
    for num in l:
        total += num
        if total > 5:
            return True
    return False


def triples_sum_to_five_4(l: list):
    """
    triples_sum_to_five_4 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and 