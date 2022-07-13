
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    
    # Your code here
    
    return lst[11]
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the even numbers in that list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list containing all the even numbers in that list.
    """
    
    # Your code here
    
    return lst[1::2]
</cell>
<cell>
# Test your code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the odd numbers in that list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list containing all the odd numbers in that list.
    """
    
    # Your code here
    
    return lst[::2]
</cell>
<cell>
# Test your code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers in the list that come after the first element in the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list containing all the numbers in the list that come after the first element in the list.
    """
    
    # Your code here
    
    return lst[1:]
</cell>
<cell>
# Test your code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers in the list that come before the first element in the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list containing all the numbers in the list that come before the first element in the list.
    """
    
    # Your code here
    
    return lst[:-1]
</cell>
<cell>
# Test your code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers in the list that come before the first element in the list. Except if the list only contains one element or is empty, return an empty list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list containing all the numbers in the list that come before the first element in the list.
    """