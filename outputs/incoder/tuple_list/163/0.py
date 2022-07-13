
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    
    return max(lst, key=lambda t: t[1])[2]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than_zero(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than zero.
    """
    
    return len([x for x in lst if x > 0])
</cell>
<cell>
count_greater_than_zero(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_than_zero(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than zero.
    """
    
    return len([x for x in lst if x < 0])
</cell>
<cell>
count_less_than_zero(lst)
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_equal_to_zero(lst):
    """
    Given a list of numbers, return the number of elements in the list that are equal to zero.
    """
    
    return len([x for x in lst if x == 0])
</cell>
<cell>
count_equal_to_zero(lst)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_than_or_equal_to_zero(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than or equal to zero.
    """
    
    return len([x for x in lst if x >= 0])
</cell>
<cell>
count_greater_than_or_equal_to_zero(lst)
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>
def count_less_than_or_equal_to_zero(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than or equal to zero.
    """
    
    return len([x for x in lst if x <= 0])
</cell>
<cell>
count_less_than_or_equal_to_zero(lst)
</cell>
<text>
Problem 12
Write a function that takes a list as an argument and returns the number of elements in the list that are evenly 