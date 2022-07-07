
def fibonacci(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    # TODO: Implement me
    pass


def fibonacci_test():
    """
    Test fibonacci()
    """
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144)]) == 144
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233)]) == 233
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377)]) == 377
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377), (15, 610)]) == 610
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377), (15, 610), (16, 987)]) == 987
    assert fibonacci([(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377),