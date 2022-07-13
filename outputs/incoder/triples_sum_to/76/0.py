
def triples_sum_to_three(l: list):
    """
    triples_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three([1, 3, 5, 0])
    False
    """
    count = 0
    for x in l:
        if x != 0:
            count += x
            if count == 3:
                return True
    return False


def triples_sum_to_four(l: list):
    """
    triples_sum_to_four takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to four, and False otherwise.

    >>> triples_sum_to_four([1, 3, 5, 0])
    True
    """
    count = 0
    for x in l:
        if x != 0:
            count += x
            if count == 4:
                return True
    return False


def triples_sum_to_five(l: list):
    """
    triples_sum_to_five takes a list of integers as an input.
    it returns True if there are 5 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five([1, 3, 5, 0])
    False
    """
    count = 0
    for x in l:
        if x != 0:
            count += x
            if count == 5:
                return True
    return False


def triples_sum_to_six(l: list):
    """
    triples_sum_to_six takes a list of integers as an input.
    it returns True if there are 6 distinct elements in the list that
    sum to six, and False otherwise.

    >>> triples_sum_to_six([1, 3, 5, 0])
    True
    """
