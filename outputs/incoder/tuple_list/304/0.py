
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return lst[11][1]
</cell>
<cell>
# Test your code
fibonacci([(5,1), (10,2), (15,3), (20,4), (25,5), (30,6), (35,7), (40,8), (45,9), (50,10)])
</cell>
<text>
Write a function that takes a list and returns a new list with only the elements that satisfy a certain condition. For example, given [1,2,3,4,5,6,7,8,9,10] and condition being greater than 5, return a new list containing [5,6,7,8,9,10].


</text>
<cell>
def conditional_list(lst, condition):
    """
    Given a list and a condition, return a new list containing only the elements that satisfy the condition.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your code
conditional_list([1,2,3,4,5,6,7,8,9,10], 5)
</cell>
<text>
Write a function that takes a list and returns a new list with all the elements multiplied by 2.


</text>
<cell>
def double_list(lst):
    """
    Given a list, return a new list containing all the elements of the list multiplied by 2.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your code
double_list([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Write a function that takes a list and returns a new list with all the elements greater than 5.


</text>
<cell>
def greater_than_five(lst):
    """
    Given a list, return a new list containing all the elements of the list greater than 5.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your code
greater_than_five([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Write a function that takes a list and returns a new list with all the elements greater than or equal to 5.


</text>
<cell>
def greater_than_or_equal_to_five(lst):
    """
    Given a list, return a new list containing all the elements of the list greater than or equal to 5.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your code
greater_than_or_equal_to_five([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Write a function that takes a list and returns a new list with all the elements less than 5.


</text>
<cell>
def 