
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    smallest_first = min(lst)
    
    return smallest_first[2]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 5
Write a function that takes a list as input and returns a new list with the second element of the tuple with the smallest first value.


</text>
<cell>
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    
    smallest_first = min(lst)
    
    return smallest_first[1]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 6
Write a function that takes a list as input and returns a new list with the second element of the tuple with the smallest second value.


</text>
<cell>
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    
    smallest_second = min(lst)
    
    return smallest_second[1]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 7
Write a function that takes a list as input and returns a new list with the third element of the tuple with the smallest third value.


</text>
<cell>
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    
    smallest_third = min(lst)
    
    return smallest_third[2]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 8
Write a function that takes a list as input and returns a new list with the third element of the tuple with the smallest third value and the second element of the tuple with the smallest second value.


</text>
<cell>
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value and the second value of the tuple with the smallest second value.
    """
    
    smallest_third = min(lst)
    
    smallest_second = min(smallest_third)
    
    return smallest_third[2], smallest_second[1]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 9
Write a function that takes a list as input and returns a new list with the third element of the tuple with the smallest third value and the second element of the tuple with the smallest second value and the first element of the tuple with the smallest first value.


</text>
<cell>
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value and the second value of the tuple with the 