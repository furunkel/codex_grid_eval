
def triples_sum_to_hundred(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    triples_sum_to_hundred_helper(l, 0, 0, 0)
    return True


def triples_sum_to_hundred_helper(l: list, sum1: int, sum2: int, sum3: int):
    """
    triples_sum_to_hundred_helper takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_helper([1, 2, -3, 7, 2, 7], 0, 0, 0, 0)
    True
    """
    if len(l) == 3:
        if sum1 + sum2 + sum3 == 100:
            return True
    return False


def triples_sum_to_hundred_helper2(l: list, sum1: int, sum2: int, sum3: int):
    """
    triples_sum_to_hundred_helper2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_helper2([1, 2, -3, 7, 2, 7], 0, 0, 0, 0)
    True
    """
    if len(l) == 3:
        if sum1 + sum2 + sum3 == 100:
            return True
    return False


def triples_sum_to_hundred_helper3(l: list, sum1: int, sum2: int, sum3: int):
    """
    triples_sum_to_hundred_helper3 takes a list of integers as an input.
    it 