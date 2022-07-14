def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    """
    return len(l) == 3 and all(x == 0 for x in l)


def triples_sum_to_one(l: list):
    """
    triples_sum_to_one takes a list of integers as an input.
    it returns True if there are exactly two distinct elements in the list
    that sum to one, and False otherwise.

    >>> triples_sum_to_one([1, 3, 5, 0])
    True
    """
    return len(l) == 2 and all(x == 1 for x in l)


def triples_sum_to_two(l: list):
    """
    triples_sum_to_two takes a list of integers as an input.
    it returns True if there are exactly two distinct elements in the list
    that sum to two, and False otherwise.

    >>> triples_sum_to_two([1, 3, 5, 0])
    True
    """
    return len(l) == 3 and all(x == 2 for x in l)


def triples_sum_to_three(l: list):
    """
    triples_sum_to_three takes a list of integers as an input.
    it returns True if there are exactly three distinct elements in the list
    that sum to three, and False otherwise.

    >>> triples_sum_to_three([1, 3, 5, 0])
    True
    """
    return len(l) == 3 and all(x == 3 for x in l)


def triples_sum_to_four(l: list):
    """
    triples_sum_to_four takes a list of integers as an input.
    it returns True if there are exactly four distinct elements in the list
    that sum to four, and False otherwise.

    >>> triples_sum_to_four([1, 3, 5, 0])
    True
    """
    return len(l) == 4 and all(x == 4 for x in l)


def triples_sum_to_five(l: list):
    """
    triples_