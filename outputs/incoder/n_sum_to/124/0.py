
def triples_sum_to_hundred(l: list):
    """
    triples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred([1, 3, 5, 0])
    False
    """
    triples = []
    for x in l:
        triples.append(x)
        if len(triples) == 3:
            triples.append(0)
            triples.sort()
            if triples[0] + triples[1] + triples[2] == 100:
                return True
    return False


@timeit
def triples_sum_to_hundred_fast(l: list):
    """
    triples_sum_to_hundred_fast takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_fast([1, 3, 5, 0])
    False
    """
    triples = []
    for x in l:
        triples.append(x)
        if len(triples) == 3:
            triples.append(0)
            triples.sort()
            if triples[0] + triples[1] + triples[2] == 100:
                return True
    return False


@timeit
def triples_sum_to_hundred_slow_2(l: list):
    """
    triples_sum_to_hundred_slow_2 takes a list of integers as an input.
    it returns True if there are 3 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> triples_sum_to_hundred_slow_2([1, 3, 5, 0])
    False
    """
    triples = []
    for x in l:
        triples.append(x)
        if len(triples) == 3:
            triples.append(0)