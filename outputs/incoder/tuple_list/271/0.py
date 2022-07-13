
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x:x[-1])[-11]

# Test Cases
print(tuple_extract(lst))
print(tuple_extract(lst2))
print(tuple_extract(lst3))
</cell>
<text>
Question 3
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than_zero(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list that are greater than zero.
    """
    return len([x for x in lst if x > 0])

# Test Cases
print(count_greater_than_zero(lst))
print(count_greater_than_zero(lst2))
print(count_greater_than_zero(lst3))
</cell>
<text>
Question 4
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_than_zero(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list that are less than zero.
    """
    return len([x for x in lst if x < 0])

# Test Cases
print(count_less_than_zero(lst))
print(count_less_than_zero(lst2))
print(count_less_than_zero(lst3))
</cell>
<text>
Question 5
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_equal_to_zero(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list that are equal to zero.
    """
    return len([x for x in lst if x == 0])

# Test Cases
print(count_equal_to_zero(lst))
print(count_equal_to_zero(lst2))
print(count_equal_to_zero(lst3))
</cell>
<text>
Question 6
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_than_or_equal_to_zero(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list that are greater than or equal to zero.
    """
    return len([x for x in lst if x >= 0])

# Test Cases
print(count_greater_than_or_equal_to_zero(lst))
print(count_greater_than_or_equal_to_zero(lst2))
print(count_greater_than_or_equal_to_zero(lst3))
</cell>
<text>
Question 7
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>