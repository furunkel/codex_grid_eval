
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    return min(lst, key=lambda x: x[1])[0]

print(some_func([(1,2), (3,4), (5,6)]))
print(some_func([(1,2), (3,4), (5,6), (7,8)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))

# Output:
# 1
# 3
# 5

# Time complexity: O(n)
# Space complexity: O(1)