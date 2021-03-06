
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest last value.
    """
    return max(lst)[1]

# Test Cases
print(min_max([(1, 2), (3, 4)]))
print(min_max([(1, 2), (3, 4), (1, 3)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12), (11, 13)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12), (11, 13), (12, 14)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12), (11, 13), (12, 14), (13, 15)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12), (11, 13), (12, 14), (13, 15), (14, 16)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 11), (10, 12), (11, 13), (12, 14), (13, 15), (14, 16), (15, 17)]))
print(min_max([(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9