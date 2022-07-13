
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    
    # Your code here
    
    return max(lst)[2]
</cell>
<cell>
some_func([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns the sum of the elements in the list.
For example, sum([1, 2, 3]) should return 6. sum([1, 2]) should return 3. sum([1, 2, 3, 4]) should return 10.


</text>
<cell>
def sum_func(lst):
    """
    Given a list of numbers, return the sum of the numbers.
    """
    
    # Your code here
    
    return sum(lst)
</cell>
<cell>
sum_func([1, 2, 3])
</cell>
<cell>
sum_func([1, 2])
</cell>
<cell>
sum_func([1, 2, 3, 4])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns the product of the elements in the list.
For example, product([1, 2, 3]) should return 6. product([1, 2]) should return 2. product([1, 2, 3, 4]) should return 24.


</text>
<cell>
def product_func(lst):
    """
    Given a list of numbers, return the product of the numbers.
    """
    
    # Your code here
    
    return product(lst)
</cell>
<cell>
product_func([1, 2, 3])
</cell>
<cell>
product_func([1, 2])
</cell>
<cell>
product_func([1, 2, 3, 4])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns the number of times the element appears in the list.
For example, count([1, 2, 3]) should return 3. count([1, 2]) should return 2. count([1, 2, 3, 4]) should return 3.


</text>
<cell>
def count_func(lst):
    """
    Given a list of numbers, return the number of times the element appears in the list.
    """
    
    # Your code here
    
    return count(lst)
</cell>
<cell>
count_func([1, 2, 3])
</cell>
<cell>
count_func([1, 2])
</cell>
<cell>
count_func([1, 2, 3, 4])
</cell>
<text>
Problem 6
Write a function that takes a list as an argument and returns the first element in the list that appears more than half of the time.
For example, first_occurence([1, 2, 3]) should return 1. first_occurence([1, 2]) should return 1. first_occurence([1, 2, 3, 4]) should return 2.


</text>
<cell>
def first_occurence_func(lst):
    """
    Given a list of numbers, return the index of the first element in the 