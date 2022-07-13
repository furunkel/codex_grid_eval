
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][2]
</cell>
<cell>
extract_value(lst)
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed.


</text>
<cell>
def reverse_list(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1], lst[-1][1]
</cell>
<cell>
reverse_list(lst)
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, sorted in ascending order.


</text>
<cell>
def reverse_list(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, sorted in ascending order.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1], lst[-1][1]
</cell>
<cell>
reverse_list(lst)
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, sorted in descending order.


</text>
<cell>
def reverse_list(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, sorted in descending order.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1], lst[-1][1]
</cell>
<cell>
reverse_list(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, sorted in ascending order and without duplicates.


</text>
<cell>
def reverse_list(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, sorted in ascending order and without duplicates.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1], lst[-1][1]
</cell>
<cell>
reverse_list(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, sorted in descending order and without duplicates.


</text>
<cell>
def reverse_list(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, sorted in descending order and 