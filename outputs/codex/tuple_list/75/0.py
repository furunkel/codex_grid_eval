
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]

print(some_func([(1, 2), (3, 4), (5, 6)]))
print(some_func([(1, 2), (3, 4), (5, 6), (7, 8)]))
print(some_func([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))

# Output:
# 2
# 4
# 6

# Time complexity: O(n)
# Space complexity: O(1)