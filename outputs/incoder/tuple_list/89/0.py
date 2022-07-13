
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(lst)[1]

# Test Cases
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5)]) == 5
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6)]) == 4
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7)]) == 6
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8)]) == 7
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9)]) == 8
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10)]) == 9
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11)]) == 10
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12)]) == 11
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13)]) == 12
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13), (1,14)]) == 13
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13), (1,14), (1,15)]) == 14
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13), (1,14), (1,15), (1,16)]) == 15
assert min_max([(5,4), (2,3), (1,5), (1,4), (2,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13), (1,14), (1,15), (1,16), (