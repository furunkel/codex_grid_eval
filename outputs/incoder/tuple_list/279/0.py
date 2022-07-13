
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    
    # your code here
    
    return twelfth_largest(lst)
</cell>
<cell>
# test your code
some_func([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Write a function that takes a list and returns a list where each element is the sum of the elements in the original list except the element at the given index.

For example, if the given list is [1,2,3,4,5], then the returned list should be [1,3,5,7,9].

If the index is out of range, return an empty list.


</text>
<cell>
def sum_except_index(lst, index):
    """
    Given a list of numbers and an index (both are ints), 
    write a function that returns the sum of all elements except the element at the given index.
    """
    
    # your code here
    
    return sum_except_index_helper(lst, index)
</cell>
<cell>
# test your code
sum_except_index([1,2,3,4,5], 2)
</cell>
<text>
Write a function that takes a list and returns a list where each element is the product of the elements in the original list except the element at the given index.

For example, if the given list is [1,2,3,4,5], then the returned list should be [1,4,10,18,25].

If the index is out of range, return an empty list.


</text>
<cell>
def product_except_index(lst, index):
    """
    Given a list of numbers and an index (both are ints), 
    write a function that returns the product of all elements except the element at the given index.
    """
    
    # your code here
    
    return product_except_index_helper(lst, index)
</cell>
<cell>
# test your code
product_except_index([1,2,3,4,5], 2)
</cell>
<text>
Write a function that takes a list and returns a list where each element is the sum of the elements in the original list except the element at the given index.

For example, if the given list is [1,2,3,4,5], then the returned list should be [1,3,5,7,9].

If the index is out of range, return an empty list.


</text>
<cell>
def sum_except_index_helper(lst, index):
    """
    Given a list of numbers and an index (both are ints), 
    write a function that returns the sum of all elements except the element at the given index.
    """
    
    # your code here
    
    return lst[:index] + lst[index+1:]
</cell>
<cell>
# test your code
sum_except_index_helper([1,2,3,4,5], 2)
</cell>
<text>
Write a function that takes a list and returns a list where each element is the product of the elements in the original list except the element at the given index.

For example, if the given list is [1,2,3,4,5], then the returned list should be 