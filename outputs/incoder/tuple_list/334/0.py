
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    lst = sorted(lst)
    return lst[11][1]
</cell>
<cell>
fibonacci([(3,1), (5,2), (8,3)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the list except for the first and last elements. For example, if the list is [1,2,3,4,5], the returned list should be [2,6,8,10,12].


</text>
<cell>
def sum_except_first(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the list except for the first and last elements.
    """
    lst = lst[1:]
    lst.append(lst[0])
    return lst
</cell>
<cell>
sum_except_first([1,2,3,4,5])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list where each element is the product of the list except for the first and last elements. For example, if the list is [1,2,3,4,5], the returned list should be [1,4,9,16,25].


</text>
<cell>
def product_except_first(lst):
    """
    Given a list of numbers, return a list where each element is the product of the list except for the first and last elements.
    """
    lst = lst[1:]
    lst.append(lst[0])
    return lst
</cell>
<cell>
product_except_first([1,2,3,4,5])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list where each element is the product of the list except for the first and last elements. For example, if the list is [1,2,3,4,5], the returned list should be [1,4,9,16,25].


</text>
<cell>
def product_except_last(lst):
    """
    Given a list of numbers, return a list where each element is the product of the list except for the first and last elements.
    """
    lst = lst[:-1]
    lst.append(lst[0])
    return lst
</cell>
<cell>
product_except_last([1,2,3,4,5])
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list where each element is the product of the list except for the first and last elements. For example, if the list is [1,2,3,4,5], the returned list should be [1,4,9,16,25].


</text>
<cell>
def product_except_first_and_last(lst):
    """
    Given a list of numbers, return a list where each element is the product of the list except for the first and last elements.
    """
    lst = lst[1:]
    lst.append(lst[0])
    return lst
</cell>
<cell>
product_