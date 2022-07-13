
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[2][2]
</cell>
<cell>
fibonacci([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with all the even numbers in that list.


</text>
<cell>
def evens(lst):
    """
    Given a list of numbers, return a list with all the even numbers in that list.
    """
    
    lst = [x for x in lst if x % 2 == 0]
    
    return lst
</cell>
<cell>
evens([1,2,3,4,5,6,7,8,9])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with all the odd numbers in that list.


</text>
<cell>
def odds(lst):
    """
    Given a list of numbers, return a list with all the odd numbers in that list.
    """
    
    lst = [x for x in lst if x % 2 != 0]
    
    return lst
</cell>
<cell>
odds([1,2,3,4,5,6,7,8,9])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by 3 but not by 5.


</text>
<cell>
def divisible_by_3_but_not_by_5(lst):
    """
    Given a list of numbers, return a list with all the numbers that are divisible by 3 but not by 5.
    """
    
    lst = [x for x in lst if x % 3 != 0 and x % 5 != 0]
    
    return lst
</cell>
<cell>
divisible_by_3_but_not_by_5([1,2,3,4,5,6,7,8,9])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by 5 but not by 3.


</text>
<cell>
def divisible_by_5_but_not_by_3(lst):
    """
    Given a list of numbers, return a list with all the numbers that are divisible by 5 but not by 3.
    """
    
    lst = [x for x in lst if x % 5 != 0 and x % 3 != 0]
    
    return lst
</cell>
<cell>
divisible_by_5_but_not_by_3([1,2,3,4,5,6,7,8,9])
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by both 3 and 5.


</text>
