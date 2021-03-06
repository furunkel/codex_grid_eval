
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    lst = sorted(lst)
    return lst[-1][1]

# Test Cases
assert fibonacci([(1, 2), (3, 5), (5, 8)]) == 8
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21)]) == 21
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5)]) == 34
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4)]) == 67
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8)]) == 100
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7)]) == 121
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6)]) == 134
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5)]) == 165
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5), (220, 4)]) == 220
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5), (220, 4), (233, 3)]) == 233
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5), (220, 4), (233, 3), (345, 2)]) == 345
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5), (220, 4), (233, 3), (345, 2), (377, 1)]) == 377
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (34, 5), (67, 4), (100, 8), (121, 7), (134, 6), (165, 5), (220, 4), (233, 3), (345, 2), (377, 1), (493, 0)]) == 493