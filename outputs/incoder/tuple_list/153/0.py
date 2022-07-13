
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    return max(lst, key=lambda t: t[0])[2]


# Test Cases
# ---------
# Write a test case for each of the cases above.
# Each test case should pass with or without printing the correct output (if any).
# Test case format:
# ('Case Name', lambda, output)
test_cases = [
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)]),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 2),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 5),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 8),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 2),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 5),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 8),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 2),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 5),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 8),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 2),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 5),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 8),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 2),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 5),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear', 8), ('orange', 2)], 8),
    ('some_func', some_func, [('apple', 3), ('banana', 5), ('pear