def triples_sum_to_two(l: list):
    """
    triples_sum_to_two takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to two, and False otherwise.

    >>> triples_sum_to_two([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and all(map(lambda x: x % 2 == 0, l))


def triples_sum_to_three(l: list):
    """
    triples_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 3 and all(map(lambda x: x % 3 == 0, l))


def triples_sum_to_four(l: list):
    """
    triples_sum_to_four takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to four, and False otherwise.

    >>> triples_sum_to_four([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 4 and all(map(lambda x: x % 4 == 0, l))


def triples_sum_to_five(l: list):
    """
    triples_sum_to_five takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to five, and False otherwise.

    >>> triples_sum_to_five([1, 3, -2, 1, 5, 8])
    True
    """
    return len(l) == 5 and all(map(lambda x: x % 5 == 0, l))


def triples_sum_to_six(l: list):
    """
    triples_sum_to_six takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to six, and False otherwise.

    >>> triples_sum_to_six([1, 3, -2, 1, 5, 8])
    True