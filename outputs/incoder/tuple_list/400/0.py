
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    lst = sorted(lst)
    return lst[-1][-1]

# Test Cases
assert fibonacci([(1, 2), (3, 5), (5, 8)]) == 8
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11)]) == 11
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53)]) == 53
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10)]) == 67
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16)]) == 101
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25)]) == 25
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33)]) == 33
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33), (197, 51)]) == 51
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33), (197, 51), (231, 67)]) == 67
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33), (197, 51), (231, 67), (269, 101)]) == 101
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33), (197, 51), (231, 67), (269, 101), (343, 163)]) == 163
assert fibonacci([(1, 2), (3, 5), (5, 8), (7, 11), (13, 21), (35, 53), (67, 10), (91, 16), (123, 25), (175, 33), (197, 51), (231, 67), (269, 101), (343, 163), (445, 253)]) == 253
assert fibonacci([(1, 2), (3, 5