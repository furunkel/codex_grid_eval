
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    
    lst = sorted(lst)
    
    return lst[11][1]
</cell>
<cell>
fibonacci([(4,2), (5,3), (6,4)])
</cell>
<text>
Problem 7
Write a function that takes a list as input and returns a list with all the even numbers in the list. For example, if the input list is [1,2,3,4,5,6,7,8,9,10], your function should return [2,4,6,8,10].


</text>
<cell>
def evens(lst):
    """
    Given a list of numbers, return a list with all the even numbers in the list.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x % 2 == 0]
</cell>
<cell>
evens([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Problem 8
Write a function that takes a list as input and returns a list with all the odd numbers in the list. For example, if the input list is [1,2,3,4,5,6,7,8,9,10], your function should return [3,5,7,9].


</text>
<cell>
def odds(lst):
    """
    Given a list of numbers, return a list with all the odd numbers in the list.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x % 2 != 0]
</cell>
<cell>
odds([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Problem 9
Write a function that takes a list as input and returns a list with all the numbers in the list that come after the first element in the list. For example, if the input list is [1,2,3,4,5,6,7,8,9,10], your function should return [2,4,6,8,10].


</text>
<cell>
def after_first(lst):
    """
    Given a list of numbers, return a list with all the numbers in the list that come after the first element in the list.
    """
    
    lst = sorted(lst)
    
    return lst[1:]
</cell>
<cell>
after_first([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Problem 10
Write a function that takes a list as input and returns a list with all the numbers in the list that come before the first element in the list. For example, if the input list is [1,2,3,4,5,6,7,8,9,10], your function should return [1,3,5,7,9].


</text>
<cell>
def before_first(lst):
    """
    Given a list of numbers, return a list with all the numbers in the list that come before the first element in the list.
    """
    
    lst = sorted(lst)
    
    return lst