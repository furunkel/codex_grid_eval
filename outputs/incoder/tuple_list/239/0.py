
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return max(lst)[2]

# Test Cases
assert min_max([(1,2,3), (4,5,6), (7,8,9)]) == 9
assert min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == 12
assert min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)]) == 15
assert min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18)]) == 18
</cell>
<text>
Problem 3
Write a function that returns the sum of the numbers in a list. For example, the list [1,2,3] returns 6.

HINT: You can use the sum function.


</text>
<cell>
def sum_nums(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    return sum(lst)

# Test Cases
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_nums([1,2,3]) == 6
assert sum_