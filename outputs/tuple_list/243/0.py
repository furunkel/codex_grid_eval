
def some_func(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[1]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))

# Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
#
# Example:
#
# >>> some_func([(1,2,3), (4,5,6), (7,8,9)])
# 2
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12)])
# 11
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)])
# 14
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18)])
# 17
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21)])
# 20
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24)])
# 23
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27)])
# 26
# >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21),