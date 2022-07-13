
def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


@test
def doubles_sum_to_hundred_with_duplicates(l: list):
    """
    doubles_sum_to_hundred_with_duplicates takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_duplicates([1])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


@test
def doubles_sum_to_hundred_with_duplicates_and_duplicates_are_not_allowed(l: list):
    """
    doubles_sum_to_hundred_with_duplicates_and_duplicates_are_not_allowed takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_duplicates_and_duplicates_are_not_allowed([1])
    False
    """
    s = 0
    for i in l:
        s += i
        if s == 100:
            return True
    return False


@test
def doubles_sum_to_hundred_with_duplicates_and_duplicates_are_allowed(l: list):
    """
    doubles_sum_to_hundred_with_duplicates_and_duplicates_are_allowed take