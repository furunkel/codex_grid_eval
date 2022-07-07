
def some_func(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[-1]

print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
print(some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]))
print(some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)]))

# Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
#
# Example:
#
#     >>> some_func([(1,2,3), (4,5,6), (7,8,9)])
#     3
#
#     >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12)])
#     12
#
#     >>> some_func([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)])
#     15
#
# """