
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: x[-1])[-2]

print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]))
print(some_func([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]))

# Output:
# 3
# 12
# 15

# Time complexity: O(n)
# Space complexity: O(1)