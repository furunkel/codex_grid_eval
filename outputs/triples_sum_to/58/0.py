
def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 2, -3, 7, 2, 7])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 2:
                        return True
    return False


def quadruples_sum_to_two_2(l: list):
    """
    quadruples_sum_to_two_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_2([1, 2, -3, 7, 2, 7])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 2:
                        return True
    return False


def quadruples_sum_to_two_3(l: list):
    """
    quadruples_sum_to_two_3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_3([1, 2, -3, 7, 2, 7])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 2:
                        return True
    return False


def quadruples_sum_to_two_4(l: list):
    """
    quadruples_sum_to_two_4