
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    
    # your code here
    
    return max(lst)[1]
</cell>
<cell>
# test your code
fibonacci([(5,1), (3,2), (1,3)])
</cell>
<text>
Problem 7
Write a function that takes a list and returns a list where each element is the sum of the elements in the original list except the element at index position in the list. For example, if the list is [1,2,3,4,5] then the returned list should be [1,3,6,10,15].


</text>
<cell>
def sum_except_index(lst, index):
    """
    Given a list and a position in the list, return the sum of all elements except the element at that position.
    """
    
    # your code here
    
    return sum(lst[:index])
</cell>
<cell>
# test your code
sum_except_index([1,2,3,4,5], 2)
</cell>
<text>
Problem 8
Write a function that takes a list and returns a list where each element is the product of the elements in the original list except the element at index position in the list. For example, if the list is [1,2,3,4,5] then the returned list should be [1,3,27,243,120].


</text>
<cell>
def product_except_index(lst, index):
    """
    Given a list and a position in the list, return the product of all the elements except the element at that position.
    """
    
    # your code here
    
    return lst[index]*lst[index+1]
</cell>
<cell>
# test your code
product_except_index([1,2,3,4,5], 2)
</cell>
<text>
Problem 9
Write a function that takes a list and returns a list where each element is the sum of the elements in the original list except the element at index position in the list. For example, if the list is [1,2,3,4,5] then the returned list should be [1,3,6,10,15].


</text>
<cell>
def sum_except_index(lst, index):
    """
    Given a list and a position in the list, return the sum of all elements except the element at that position.
    """
    
    # your code here
    
    return sum(lst[:index])
</cell>
<cell>
# test your code
sum_except_index([1,2,3,4,5], 2)
</cell>
<text>
Problem 10
Write a function that takes a list and returns a list where each element is the product of the elements in the original list except the element at index position in the list. For example, if the list is [1,2,3,4,5] then the returned list should be [1,3,27,243,120].


</text>
<cell>
def product_except_index(lst, index):
    """
    Given a list and a position in the list, return the product of all the elements except the element 