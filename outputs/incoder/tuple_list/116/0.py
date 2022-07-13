
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1]
</cell>
<cell>
f(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the sum of the numbers in the list. For example, sum([1, 2, 3]) should return 6.

Hint: use the sum() function!


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    
    return sum(lst)
</cell>
<cell>
f(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the product of the numbers in the list. For example, product([1, 2, 3]) should return 6. Hint: use the product() function!


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return the product of the numbers in the list.
    """
    
    return product(lst)
</cell>
<cell>
f(lst)
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of items in the list that are not in the list [3, 4, 5]. For example, count_not_in([1, 2, 3, 4], 3) should return 1.


</text>
<cell>
def f(lst, lst2):
    """
    Given a list of numbers, return the number of items in the list that are not in the list [3, 4, 5].
    """
    
    return len(lst) - len(set(lst) & set(lst2))
</cell>
<cell>
f(lst, lst2)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list of all the numbers in the list that are less than the number 10. For example, list_less_than([1, 2, 3, 10, 4, 5], 10) should return [1, 4, 5].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list of the numbers in the list that are less than 10.
    """
    
    return list(filter(lambda x: x<10, lst))
</cell>
<cell>
f(lst)
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list of all the numbers in the list that are less than or equal to the number 10. For example, list_less_than_or_equal_to([1, 2, 3, 10, 4, 5], 10) should return [1, 4, 5].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list of the numbers in the list that are less than or equal to 10.
    """
    
    return list(filter(lambda x: x<=10, lst))
</cell>
<cell>
f(lst)
</cell>
<text>
