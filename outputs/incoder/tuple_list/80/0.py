
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(lst, key=lambda t: t[0])[1]


# Test Cases
# Test Case 1
assert f([(3, 'a'), (2, 'b'), (1, 'c')]) == 'c'
# Test Case 2
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a')]) == 'a'
# Test Case 3
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c')]) == 'c'
# Test Case 4
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b')]) == 'b'
# Test Case 5
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a')]) == 'a'
# Test Case 6
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b')]) == 'b'
# Test Case 7
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a')]) == 'a'
# Test Case 8
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a'), (0, 'b')]) == 'b'
# Test Case 9
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a'), (0, 'b'), (0, 'c')]) == 'c'
# Test Case 10
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a'), (0, 'b'), (0, 'c'), (2, 'a')]) == 'a'
# Test Case 11
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a'), (0, 'b'), (0, 'c'), (2, 'a'), (1, 'b')]) == 'b'
# Test Case 12
assert f([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'a'), (2, 'c'), (1, 'b'), (0, 'a'), (2, 'b'), (1, 'a'), (0, 'b'), (0, 'c'), 