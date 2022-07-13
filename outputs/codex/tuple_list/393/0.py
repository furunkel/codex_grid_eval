
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x: x[2])[-1]

print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]))
print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]))

# Output:
# 3
# 12
# 15

# Explanation:
# The third value of each tuple is the largest in the list, so the last value of the tuple with the largest third value is returned.