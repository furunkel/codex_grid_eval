
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    
    lst = sorted(lst)
    return lst[-1][-1]
</cell>
<cell>
min_max([(3,4),(5,6),(7,8)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than zero.
    """
    
    lst = sorted(lst)
    return len([x for x in lst if x > 0])
</cell>
<cell>
count_greater_than_zero([(3,4),(5,6),(7,8)])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_than_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than zero.
    """
    
    lst = sorted(lst)
    return len([x for x in lst if x < 0])
</cell>
<cell>
count_less_than_zero([(3,4),(5,6),(7,8)])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_equal_to_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are equal to zero.
    """
    
    lst = sorted(lst)
    return len([x for x in lst if x == 0])
</cell>
<cell>
count_equal_to_zero([(3,4),(5,6),(7,8)])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_than_or_equal_to_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than or equal to zero.
    """
    
    lst = sorted(lst)
    return len([x for x in lst if x >= 0])
</cell>
<cell>
count_greater_than_or_equal_to_zero([(3,4),(5,6),(7,8)])
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>
def count_less_than_or_equal_to_zero(