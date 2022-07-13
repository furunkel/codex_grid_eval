
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[1])[2]
</cell>
<cell>
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 7
Write a function that takes a list and returns a new list with all of the elements of the list sorted from smallest to largest.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted from smallest to largest.
    """
    
    # Your code here
    
    return sorted(lst)
</cell>
<cell>
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 8
Write a function that takes a list and returns a new list with all of the elements of the list sorted from largest to smallest.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted from largest to smallest.
    """
    
    # Your code here
    
    return sorted(lst, key=lambda x: -x[1])
</cell>
<cell>
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 9
Write a function that takes a list and returns a new list with all of the elements of the list sorted from smallest to largest.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted from smallest to largest.
    """
    
    # Your code here
    
    return sorted(lst, key=lambda x: x[0])
</cell>
<cell>
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 10
Write a function that takes a list and returns a new list with all of the elements of the list sorted from largest to smallest.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted from largest to smallest.
    """
    
    # Your code here
    
    return sorted(lst, key=lambda x: -x[0])
</cell>
<cell>
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Problem 11
Write a function that takes a list and returns a new list with all of the elements of the list sorted from smallest to largest.


</text>
<cell>
def some_func(lst):
    """
