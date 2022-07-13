
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

print(some_func([(1, 2), (2, 3), (3, 4)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13)]))
print(some_func([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7