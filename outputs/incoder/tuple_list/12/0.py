
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    lst = sorted(lst)
    return lst[0][0]

# Test Cases
assert extract_value([]) == None
assert extract_value([1]) == 1
assert extract_value([(1, 2), (3, 4)])  == 3
assert extract_value([(1, 2), (3, 4), (1, 2)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23), (24, 25)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23), (24, 25), (26, 27)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23), (24, 25), (26, 27), (28, 29)])  == 3
assert extract_value([(1, 2), (3, 4), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23), (24, 25), (26, 27), (28, 