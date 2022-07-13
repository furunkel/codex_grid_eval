
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    
    return max(lst)[2]
</cell>
<cell>
min_max(lst)
</cell>
<text>
Problem 4
Write a function that takes a list as input and returns a new list with the elements of the list that satisfy the condition of being even.


</text>
<cell>
def even_lst(lst):
    """
    Given a list of tuples, write a function that returns the elements of the list that satisfy the condition of being even.
    """
    
    return [x for x in lst if x[1] % 2 == 0]
</cell>
<cell>
even_lst(lst)
</cell>
<text>
Problem 5
Write a function that takes a list as input and returns a new list with the elements of the list that satisfy the condition of being odd.


</text>
<cell>
def odd_lst(lst):
    """
    Given a list of tuples, write a function that returns the elements of the list that satisfy the condition of being odd.
    """
    
    return [x for x in lst if x[1] % 2 != 0]
</cell>
<cell>
odd_lst(lst)
</cell>
<text>
Problem 6
Write a function that takes a list as input and returns a new list with the elements of the list that satisfy the condition of being divisible by 3.


</text>
<cell>
def div_lst(lst):
    """
    Given a list of tuples, write a function that returns the elements of the list that satisfy the condition of being divisible by 3.
    """
    
    return [x for x in lst if x[1] % 3 == 0]
</cell>
<cell>
div_lst(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as input and returns a new list with the elements of the list that satisfy the condition of being divisible by 5.


</text>
<cell>
def div_lst(lst):
    """
    Given a list of tuples, write a function that returns the elements of the list that satisfy the condition of being divisible by 5.
    """
    
    return [x for x in lst if x[1] % 5 == 0]
</cell>
<cell>
div_lst(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as input and returns a new list with the elements of the list that satisfy the condition of being divisible by 7.


</text>
<cell>
def div_lst(lst):
    """
    Given a list of tuples, write a function that returns the elements of the list that satisfy the condition of being divisible by 7.
    """
    
    return [x for x in lst if x[1] % 7 == 0]
</cell>
<cell