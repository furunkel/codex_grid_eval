
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    
    # Your code here
    
    return lst[2]

# Test case
assert extract_value([(7, 3, 9), (5, 2, 8), (4, 1, 6), (6, 3, 8), (7, 1, 5), (6, 2, 4), (5, 3, 6)]) == 8
</cell>
<text>
Problem 7
Write a function that takes a list and returns a new list with all of the elements of the list sorted in descending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted in descending order.
    """
    
    # Your code here
    
    return lst
    
# Test case
assert sort_list([(7, 3, 9), (5, 2, 8), (4, 1, 6), (6, 3, 8), (7, 1, 5), (6, 2, 4), (5, 3, 6)]) == [6, 5, 4, 3, 2, 7, 8, 9]
</cell>
<text>
Problem 8
Write a function that takes a list and returns a new list with all of the elements of the list sorted in ascending order.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted in ascending order.
    """
    
    # Your code here
    
    return lst
    
# Test case
assert sort_list([(7, 3, 9), (5, 2, 8), (4, 1, 6), (6, 3, 8), (7, 1, 5), (6, 2, 4), (5, 3, 6)]) == [7, 8, 6, 4, 6, 5, 3, 2, 1]
</cell>
<text>
Problem 9
Write a function that takes a list and returns a new list with all of the elements of the list sorted in descending order, but only if the elements of the list are tuples.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted in descending order, but only if the elements of the list are tuples.
    """
    
    # Your code here
    
    return lst
    
# Test case
assert sort_list([(7, 3, 9), (5, 2, 8), (4, 1, 6), (6, 3, 8), (7, 1, 5), (6, 2, 4), (5, 3, 6)]) == [6, 5, 4, 3, 2, 7, 8, 9]
</cell>
<text>
Problem 10
Write a function that takes a list and returns a new list with all of the elements of the list sorted in ascending order, but only if the elements of the list are tuples.


</text>
<cell>
def sort_list(lst):
    """
    Given a list of tuples, write a function that returns a new list with all of the elements of the list sorted in 