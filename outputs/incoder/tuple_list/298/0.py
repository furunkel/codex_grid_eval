
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return lst[11][1]
</cell>
<cell>
fibonacci([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with all the even numbers in that list.


</text>
<cell>
def evens(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return [x for x, y in lst if y%2 == 0]
</cell>
<cell>
evens([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with all the odd numbers in that list.


</text>
<cell>
def odds(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return [x for x, y in lst if y%2 != 0]
</cell>
<cell>
odds([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with all the even numbers that are less than the sum of the first 10 numbers in the list.


</text>
<cell>
def even_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return [x for x, y in lst if y%2 == 0 and x < sum(lst[:10])]
</cell>
<cell>
even_sum([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with all the odd numbers that are less than the sum of the first 10 numbers in the list.


</text>
<cell>
def odd_sum(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return [x for x, y in lst if y%2 != 0 and x < sum(lst[:10])]
</cell>
<cell>
odd_sum([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list with all the even numbers that are 