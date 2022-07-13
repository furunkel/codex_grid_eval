
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    return min(lst)[1]
</cell>
<cell>
min_max([(4,5), (6,7), (8,9)])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a tuple with the first and last element of the list. 
For example, if the list was [1,2,3,4,5], the function should return (1,5).


</text>
<cell>
def first_last(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple.
    """
    
    return lst[0], lst[-1]
</cell>
<cell>
first_last([1,2,3,4,5])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a tuple with the first and last element of the list sorted in ascending order.
For example, if the list was [1,2,3,4,5], the function should return (1,5).


</text>
<cell>
def first_last_sorted(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple sorted in ascending order.
    """
    
    return lst[0], lst[-1]
</cell>
<cell>
first_last_sorted([1,2,3,4,5])
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns a tuple with the first and last element of the list sorted in descending order.
For example, if the list was [1,2,3,4,5], the function should return (5,4).


</text>
<cell>
def first_last_sorted(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple sorted in descending order.
    """
    
    return lst[-1], lst[0]
</cell>
<cell>
first_last_sorted([1,2,3,4,5])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a tuple with the first and last element of the list sorted in ascending order by the second value of the tuple.
For example, if the list was [(1, 2), (3, 4)], the function should return ((1, 2), (3, 4)).


</text>
<cell>
def first_last_sorted(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple sorted in ascending order by the second value of the tuple.
    """
    
    return sorted(lst)
</cell>
<cell>
first_last_sorted([(1, 2), (3, 4)])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a tuple with the first and last element of the list sorted in descending order by the second value of the tuple.
For example, if the list was [(1, 2), (3, 4)], the function should return ((3, 4