
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest second value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1]
</cell>
<cell>
fibonacci([(5,3), (2,1), (6,5)])
</cell>
<text>
Problem 7: Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to 10.


</text>
<cell>
def count_less_than_ten(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than or equal to 10.
    """
    
    lst = sorted(lst)
    
    return len([x for x in lst if x <= 10])
</cell>
<cell>
count_less_than_ten([(5,3), (2,1), (6,5)])
</cell>
<text>
Problem 8: Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to 10.


</text>
<cell>
def count_greater_than_ten(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than or equal to 10.
    """
    
    lst = sorted(lst)
    
    return len([x for x in lst if x >= 10])
</cell>
<cell>
count_greater_than_ten([(5,3), (2,1), (6,5)])
</cell>
<text>
Problem 9: Write a function that takes a list as an argument and returns the number of elements in the list that are divisible by 3.


</text>
<cell>
def count_divisible_by_three(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are divisible by 3.
    """
    
    lst = sorted(lst)
    
    return len([x for x in lst if x % 3 == 0])
</cell>
<cell>
count_divisible_by_three([(5,3), (2,1), (6,5)])
</cell>
<text>
Problem 10: Write a function that takes a list as an argument and returns the number of elements in the list that are divisible by 5 and not divisible by 3.


</text>
<cell>
def count_divisible_by_five(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are divisible by 5 and not divisible by 3.
    """
    
    lst = sorted(lst)
    
    return len([x for x in lst if x % 5 == 0 and x % 3 != 0])
</cell>
<cell>
count_divisible_by_five([(5,3), (2,1), (6,5)])
</cell>
<text>
Problem 11