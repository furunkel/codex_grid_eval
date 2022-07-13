
def quadruples_sum_to_hundred(l: list):
    """
    quadruples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> quadruples_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    l = sorted(l)
    sum = 0
    count = 0
    for i in range(len(l)):
        sum += l[i]
        if sum >= 100:
            count += 1
            sum -= 100
    if count == 4:
        return True
    else:
        return False


def quadruples_sum_to_hundred_list(l: list):
    """
    quadruples_sum_to_hundred_list takes a list of integers as an input.
    it returns a list of quadruples that sum to hundred.

    >>> quadruples_sum_to_hundred_list([1, 3, -2, 1, 5, 8])
    [(1, 3, -2, 1, 5, 8)]
    """
    l = sorted(l)
    sum = 0
    count = 0
    quadruples = []
    for i in range(len(l)):
        sum += l[i]
        if sum >= 100:
            count += 1
            sum -= 100
            quadruples.append((l[i], l[i + 1], l[i + 2], l[i + 3]))
    if count == 4:
        return quadruples
    else:
        return None


def quadruples_sum_to_hundred_list_2(l: list):
    """
    quadruples_sum_to_hundred_list_2 takes a list of integers as an input.
    it returns a list of quadruples that sum to hundred.

    >>> quadruples_sum_to_hundred_list_2([1, 3, -2, 1, 5, 8])
    [(1, 3, -2, 1, 5, 8)]
