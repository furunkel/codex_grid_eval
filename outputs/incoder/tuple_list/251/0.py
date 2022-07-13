
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst)[2]

# Test Cases
print(min_max([(1,2,3), (4,5,6), (7,8,9)]))
print(min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]))
print(min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)]))
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than zero.
    """
    return len([x for x in lst if x > 0])

# Test Cases
print(count_greater_than_zero([1,2,3]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_than_zero([1,2,3, 0]))
print(count_greater_