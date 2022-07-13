
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return lst[-1][-1]
</cell>
<cell>
fibonacci([(3,5), (4,6), (5,7)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with all the even numbers in that list.


</text>
<cell>
def evens(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x[0]%2==0]
</cell>
<cell>
evens([(3,5), (4,6), (5,7)])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with all the odd numbers in that list.


</text>
<cell>
def odds(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x[0]%2!=0]
</cell>
<cell>
odds([(3,5), (4,6), (5,7)])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by 7 in that list.


</text>
<cell>
def divisible_by_7(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x[0]%7==0]
</cell>
<cell>
divisible_by_7([(3,5), (4,6), (5,7)])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by 3 in that list.


</text>
<cell>
def divisible_by_3(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    
    lst = sorted(lst)
    
    return [x for x in lst if x[0]%3==0]
</cell>
<cell>
divisible_by_3([(3,5), (4,6), (5,7)])
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list with all the numbers that are divisible by 5 in that list.


</text>
<cell>
def divisible_by_5(