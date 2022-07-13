
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest eleventh value.
    """
    
    # your code here
    
    return lst[1]
</cell>
<cell>
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed.
    """
    
    # your code here
    
    return lst[::-1]
</cell>
<cell>
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, followed by the elements of the list separated by commas.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, followed by the elements of the list separated by commas.
    """
    
    # your code here
    
    return lst[::-1] + ', ' + ', '.join(lst)
</cell>
<cell>
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, and so on.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, and so on.
    """
    
    # your code here
    
    return lst[::-1] + ', ' + ', '.join(lst) + ', ' + ', '.join(lst)
</cell>
<cell>
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns a list with the first and last element of the list reversed, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, and so on.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first and last value of the tuple reversed, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, followed by the elements of the list separated by commas, and so on.
    """
    
    # your code here
    
    return lst[::-1]