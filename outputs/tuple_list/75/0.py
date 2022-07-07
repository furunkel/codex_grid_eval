
def some_func(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]

print(some_func([(1, 'a'), (2, 'b'), (3, 'c')]))
print(some_func([(3, 'c'), (1, 'a'), (2, 'b')]))
print(some_func([(2, 'b'), (1, 'a'), (3, 'c')]))

# Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
#
# >>> some_func([(1, 'a'), (2, 'b'), (3, 'c')])
# 'a'
# >>> some_func([(3, 'c'), (1, 'a'), (2, 'b')])
# 'a'
# >>> some_func([(2, 'b'), (1, 'a'), (3, 'c')])
# 'a'