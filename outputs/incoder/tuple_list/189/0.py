
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[2])[2]
</cell>
<cell>
some_func([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the numbers in the list. For example, some_func([1,2,3]) should return [1,2,3].

Hint: You can use the map function and a list comprehension.


</text>
<cell>
def some_func(lst):
    """
    Given a list of numbers, return the squared sum of the numbers.
    """
    
    # Your code here
    
    return list(map(lambda x: x**2, lst))
</cell>
<cell>
some_func([1,2,3])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list where each element is the sum of the numbers in the list. For example, some_func([1,2,3]) should return [3,4,7].

Hint: You can use the sum function and a list comprehension.


</text>
<cell>
def some_func(lst):
    """
    Given a list of numbers, return the sum of the numbers.
    """
    
    # Your code here
    
    return list(map(lambda x: sum(x), lst))
</cell>
<cell>
some_func([1,2,3])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list where each element is the product of the numbers in the list. For example, some_func([1,2,3]) should return [1,2,6].

Hint: You can use the product function and a list comprehension.


</text>
<cell>
def some_func(lst):
    """
    Given a list of numbers, return the product of the numbers.
    """
    
    # Your code here
    
    return list(map(lambda x: product(x), lst))
</cell>
<cell>
some_func([1,2,3])
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns a list where each element is the product of the numbers in the list. For example, some_func([1,2,3]) should return [1,2,6].

Hint: You can use the product function and a list comprehension.


</text>
<cell>
def some_func(lst):
    """
    Given a list of numbers, return the product of the numbers.
    """
    
    # Your code here
    
    return list(map(lambda x: product(x), lst))
</cell>
<cell>
some_func([1,2,3])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the 