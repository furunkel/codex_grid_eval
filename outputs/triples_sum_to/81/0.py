
def quadruples_sum_to_three(l: list):
    """
    quadruples_sum_to_three takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three([1, 3, -2, 1, 5, 8])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 3:
                        return True
    return False


def quadruples_sum_to_three_2(l: list):
    """
    quadruples_sum_to_three_2 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three_2([1, 3, -2, 1, 5, 8])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 3:
                        return True
    return False


def quadruples_sum_to_three_3(l: list):
    """
    quadruples_sum_to_three_3 takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to three, and False otherwise.

    >>> quadruples_sum_to_three_3([1, 3, -2, 1, 5, 8])
    True
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                for m in range(k + 1, len(l)):
                    if l[i] + l[j] + l[k] + l[m] == 3:
                        return True
    return False


def quadruples_sum_to_three_4(l: list):
    """
    quadruples_sum_to_three_4