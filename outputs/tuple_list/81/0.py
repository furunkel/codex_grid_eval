
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    return max(text, key=lambda x: x[0])[1]

print(some_func([(1, 'a'), (2, 'b'), (3, 'c')]))
print(some_func([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]))
print(some_func([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]))

# Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
#
# Example:
#
# >>> some_func([(1, 'a'), (2, 'b'), (3, 'c')])
# 'c'
# >>> some_func([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
# 'd'
# >>> some_func([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
# 'e'