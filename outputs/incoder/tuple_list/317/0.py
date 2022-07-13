
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    
    return min(lst, key=lambda x:x[2])[1]
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the number of elements in the list that have a third value that is less than 5.


</text>
<cell>
def count_less_than_five(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that have a third value that is less than 5.
    """
    
    return len([x for x in lst if x[2] < 5])
</cell>
<cell>
count_less_than_five([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the number of elements in the list that have a third value that is less than or equal to 5.


</text>
<cell>
def count_less_than_or_equal_five(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that have a third value that is less than or equal to 5.
    """
    
    return len([x for x in lst if x[2] <= 5])
</cell>
<cell>
count_less_than_or_equal_five([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list that have a third value that is greater than 5.


</text>
<cell>
def count_greater_than_five(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that have a third value that is greater than 5.
    """
    
    return len([x for x in lst if x[2] > 5])
</cell>
<cell>
count_greater_than_five([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements in the list that have a third value that is greater than or equal to 5.


</text>
<cell>
def count_greater_than_or_equal_five(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that have a third value that is greater than or equal to 5.
    """
    
    return len([x for x in lst if x[2] >= 5])
</cell>
<cell>
count_greater_than_or_equal_five([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the 