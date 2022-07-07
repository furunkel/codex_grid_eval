
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[-1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values after the first value greater than 8.
    """
    return [x[1] for x in text if x[0] > 8]


def remove_negatives(text):
    """
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
    """
    return [x for x in text if x > 0]


def remove_negatives_in_place(text):
    """
    Given a list of numbers, write a function that removes any negative numbers from that list and returns the result.
    """
    return [x for x in text if x > 0]


def order_by_magnitude(text):
    """
    Given a list of numbers, write a function that returns a list where the elements are sorted in descending order.
    """
    return sorted(text, reverse=True)


def matrix_addition(text):
    """
    Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of adding the two matrices.
    The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.
    Example: to add
    1 2
    3 4
    and
    5 6
    7 8
    you should return a new 2x2 matrix
    6 8
    10 12
    """
    return [[x + y for x, y in zip(a, b)] for a, b in zip(text[0], text[1])]


def matrix_addition_in_place(text):
    """
    Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of adding the two matrices.
    The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.
    Example: to add
    1 2
    3 4
    and
    5 6
    7 8
    you should return a new 2x2 matrix
    6 8
    10 12
    """