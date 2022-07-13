
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return min(lst)
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
tuple_extract(lst)
</cell>
<text>
Write a function that returns the second value of the tuple with the smallest second value.


</text>
<cell>
def tuple_second_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return min(lst)[1]
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
tuple_second_value(lst)
</cell>
<text>
Write a function that returns a list of all the second values of the tuples in an input list of tuples.


</text>
<cell>
def tuple_second_values(lst):
    """
    Given a list of tuples, write a function that returns a list of all the second values of the tuples in an input list of tuples.
    """
    
    # Your code here
    
    return list(map(lambda x:x[1], [x for x in lst]))
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
tuple_second_values(lst)
</cell>
<text>
Write a function that returns a list of all the values in the first element of the tuples in an input list of tuples.


</text>
<cell>
def tuple_first_values(lst):
    """
    Given a list of tuples, write a function that returns a list of all the values in the first element of the tuples in an input list of tuples.
    """
    
    # Your code here
    
    return list(map(lambda x:x[0], [x for x in lst]))
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
tuple_first_values(lst)
</cell>
<text>
Write a function that returns a list of all the values in the second element of the tuples in an input list of tuples.


</text>
<cell>
def tuple_second_elements(lst):
    """
    Given a list of tuples, write a function that returns a list of all the values in the second element of the tuples in an input list of tuples.
    """
    
    # Your code here
    
    return list(map(lambda x:x[2], lst))
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
tuple_second_elements(lst)
</cell>
<text>
Write a function that returns a list of all the values in the first and second element of the tuple