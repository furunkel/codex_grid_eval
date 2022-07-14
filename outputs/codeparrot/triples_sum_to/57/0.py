def quadruples_sum_to_two(l: list):
    """
    quadruples_sum_to_two takes a list of integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two([1, 3, -2, 1, 5, 8])
    False
    """
    return sum(l) % 2 == 0


def quadruples_sum_to_two_with_one_element(l: list):
    """
    quadruples_sum_to_two_with_one_element takes a list of integers as an
    input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_with_one_element([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 1


def quadruples_sum_to_two_with_two_elements(l: list):
    """
    quadruples_sum_to_two_with_two_elements takes a list of integers as an
    input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_with_two_elements([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 2


def quadruples_sum_to_two_with_two_elements_with_one_element(l: list):
    """
    quadruples_sum_to_two_with_two_elements_with_one_element takes a list of
    integers as an input.
    it returns True if there are 4 distinct elements in the list that
    sum to two, and False otherwise.

    >>> quadruples_sum_to_two_with_two_elements_with_one_element([1, 3, -2, 1, 5, 8])
    True
    """
    return sum(l) % 2 == 1


def quadruples_sum_to_two_with_two_elements_with_two_elements_with