
def doubles_sum_to_hundred(l: list):
    """
    doubles_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred([1, 3, -2, 1, 5, 8])
    False
    """
    count = 0
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            count += 1
            sum -= 100
    return count == 2


@given(integers(min_value=-100, max_value=100))
@example(100)
@example(-100)
def doubles_sum_to_hundred_with_negative(l: list):
    """
    doubles_sum_to_hundred_with_negative takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_negative([1, 3, -2, 1, 5, 8])
    False
    """
    count = 0
    sum = 0
    for i in l:
        sum += i
        if sum > 100:
            count += 1
            sum -= 100
    return count == 2


@given(integers(min_value=-100, max_value=100))
@example(100)
@example(-100)
def doubles_sum_to_hundred_with_negative_and_negative(l: list):
    """
    doubles_sum_to_hundred_with_negative_and_negative takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> doubles_sum_to_hundred_with_negative_and_negative([1, 3, -2, 1, 5, 8])