def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1, 3, 5, 0])
    False
    """
    return len(l) == 2 and l[0] == l[1]


def doubles_sum_to_two_with_one_element(l: list):
    """
    doubles_sum_to_two_with_one_element takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_with_one_element([1, 3, 5, 0])
    True
    """
    return len(l) == 1 and l[0] == l[1]


def doubles_sum_to_two_with_two_elements(l: list):
    """
    doubles_sum_to_two_with_two_elements takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_with_two_elements([1, 3, 5, 0])
    True
    """
    return len(l) == 2 and l[0] == l[1] and l[0] == l[2]


def doubles_sum_to_two_with_two_elements_with_one_element(l: list):
    """
    doubles_sum_to_two_with_two_elements_with_one_element takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two_with_two_elements_with_one_element([1, 3, 5, 0])
    True
    """
    return len(l) == 2 and l[0] == l[1] and l[0] == l[2] and l[1] == l[3]


def doubles_sum_to_two_