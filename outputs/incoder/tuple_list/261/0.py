
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return max(lst)[2]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 4
Write a function that takes a list and returns a new list with all of the elements of the given list except the first and last.

For example, given [1,2,3,4,5], return [2,3,4,5].


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return lst[1:]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 5
Write a function that takes a list and returns a new list with all of the elements of the given list except the elements with index values that are not even.

For example, given [1,2,3,4,5], return [1,3,5].


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return lst[1::2]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 6
Write a function that takes a list and returns a new list with all of the elements of the given list except the elements with index values that are less than 0.

For example, given [1,2,3,4,5], return [2,4,5].


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return lst[::2]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 7
Write a function that takes a list and returns a new list with all of the elements of the given list except the elements with index values that are greater than or equal to 3.

For example, given [1,2,3,4,5], return [1,2,4].


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return lst[3::4]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
