def triples_sum_to_three(l: list):
    """
    triples_sum_to_three takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three([1, 2, -3, 7, 2, 7])
    False
    """
    return len(l) == 3 and all(x == y for x, y in zip(l[0], l[1]))


def triples_sum_to_two(l: list):
    """
    triples_sum_to_two takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to two, and False otherwise.

    >>> triples_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and all(x == y for x, y in zip(l[0], l[1]))


def triples_sum_to_three_with_one_of_two(l: list):
    """
    triples_sum_to_three_with_one_of_two takes a list of integers as an
    input.
    it returns True if there are three distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three_with_one_of_two([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 3 and all(x == y for x, y in zip(l[0], l[1]))


def triples_sum_to_three_with_two_of_one_of_two(l: list):
    """
    triples_sum_to_three_with_two_of_one_of_two takes a list of integers as
    an input.
    it returns True if there are three distinct elements in the list that
    sum to three, and False otherwise.

    >>> triples_sum_to_three_with_two_of_one_of_two([1, 2, -3, 7, 2, 7])
    True
    """
    return len(l) == 2 and all(x == y for x, y in zip(l[0], l[1]))