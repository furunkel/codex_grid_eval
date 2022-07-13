
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest last value.
    """
    return min(lst)[2]
</cell>
<cell>
min_max(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than zero.
    """
    return len([x for x in lst if x[1] > 0])
</cell>
<cell>
count_greater_zero(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than zero.
    """
    return len([x for x in lst if x[1] < 0])
</cell>
<cell>
count_less_zero(lst)
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are equal to zero.
    """
    return len([x for x in lst if x[1] == 0])
</cell>
<cell>
count_zero(lst)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_equal_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than or equal to zero.
    """
    return len([x for x in lst if x[1] >= 0])
</cell>
<cell>
count_greater_equal_zero(lst)
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>
def count_less_equal_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than or equal to zero.
    """
    return len([x for x in lst if x[1] < 0])
</cell>
<cell>
count_less_equal_zero(lst)
</cell>
<text>
Problem 12
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are 