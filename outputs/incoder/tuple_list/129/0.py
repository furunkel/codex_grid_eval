
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[1])[11]
</cell>
<cell>
some_func([(7, 1), (8, 2), (9, 3), (10, 4), (11, 5), (12, 6)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the numbers in the list. For example, sum([1, 2, 3]) should return 6. Make sure to use only addition and multiplication operators.


</text>
<cell>
def sum_func(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    
    # Your code here
    
    return sum(lst)
</cell>
<cell>
sum_func([1, 2, 3])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list where each element is the product of the numbers in the list. For example, product([1, 2, 3]) should return 6. Make sure to use only multiplication and division operators.


</text>
<cell>
def product_func(lst):
    """
    Given a list of numbers, return the product of the numbers in the list.
    """
    
    # Your code here
    
    return product(lst)
</cell>
<cell>
product_func([1, 2, 3])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list where each element is the sum of all the numbers in the list that are less than the value of the element. For example, sum([1, 2, 3, 4], 4) should return 10. Make sure to use only addition and multiplication operators.


</text>
<cell>
def sum_less_func(lst, val):
    """
    Given a list of numbers and a value, return the sum of all the numbers in the list that are less than the value.
    """
    
    # Your code here
    
    return sum(lst)
</cell>
<cell>
sum_less_func([1, 2, 3, 4], 4)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list where each element is the product of the numbers in the list that are less than the value of the element. For example, product([1, 2, 3, 4], 4) should return 24. Make sure to use only multiplication and division operators.


</text>
<cell>
def product_less_func(lst, val):
    """
    Given a list of numbers and a value, return the product of the numbers in the list that are less than the value.
    """
    
    # Your code here
    
    return product(lst)
</cell>
<cell>
product_less_func([1, 2, 3, 4], 4)
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list where each element 