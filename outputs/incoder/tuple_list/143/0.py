
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest last value.
    """
    
    return max(lst)[1]
</cell>
<cell>
min_max([(5,5), (4,4), (3,3), (2,2), (1,1)])
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list with all the numbers of the list sorted in ascending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of numbers, return a list with all the numbers of the list sorted in ascending order.
    """
    
    return sorted(lst)
</cell>
<cell>
sort_list([5,4,3,2,1])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list with all the numbers of the list sorted in descending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of numbers, return a list with all the numbers of the list sorted in descending order.
    """
    
    return sorted(lst, reverse=True)
</cell>
<cell>
sort_list([5,4,3,2,1])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list with all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of numbers, return a list with all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order.
    """
    
    return sorted(lst), sorted(lst, reverse=True)
</cell>
<cell>
sort_list([5,4,3,2,1])
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns a list with all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order and all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of numbers, return a list with all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order and all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending order.
    """
    
    return sorted(lst), sorted(lst, reverse=True), sorted(lst), sorted(lst, reverse=True)
</cell>
<cell>
sort_list([5,4,3,2,1])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with all the numbers of the list sorted in ascending order and all the numbers of the list sorted in descending 