
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    
    smallest_twelfth = lst[0][2]
    
    for tup in lst:
        if tup[2] < smallest_twelfth:
            smallest_twelfth = tup[2]
    
    return smallest_twelfth
</cell>
<cell>
# Test your code
lst = [(1, 2), (4, 5), (7, 8), (10, 11)]
print(tuple_extract(lst))
</cell>
<text>
Tuples as Lists
A tuple is similar to a list, but you use parentheses to denote the tuple. Once you have created the tuple, you can unpack it by assigning it to a variable. Here is an example:


</text>
<cell>
# Create a tuple
t = (1, 2, 3)
</cell>
<text>
You can unpack the tuple by assigning it to a variable. Remember that you can assign multiple variables at once:


</text>
<cell>
a, b, c = t
</cell>
<text>
You can also unpack multiple values from a tuple:


</text>
<cell>
nums = (1, 2, 3, 4, 5)
a, b, c, d, e = nums
</cell>
<text>
Exercise
Write a function that returns the first element of a tuple.


</text>
<cell>
# Solution

def tuple_first(tuple):
    """
    Given a tuple, return the value of the first element in the tuple.
    """
    
    return tuple[0]
</cell>
<cell>
# Test your code
print(tuple_first((1, 2, 3, 4)))
</cell>
<text>
Exercise
Write a function that returns a tuple where each element is the sum of the elements of the original tuple.


</text>
<cell>
# Solution

def tuple_sum(tuple):
    """
    Given a tuple, return the sum of the elements in the tuple.
    """
    
    sum = 0
    
    for num in tuple:
        sum += num
    
    return sum
</cell>
<cell>
# Test your code
print(tuple_sum((1, 2, 3, 4, 5)))
</cell>
<text>
Exercise
Write a function that returns a tuple where each element is the product of the elements of the original tuple.


</text>
<cell>
# Solution

def tuple_product(tuple):
    """
    Given a tuple, return the product of the elements in the tuple.
    """
    
    product = 1
    
    for num in tuple:
        product *= num
    
    return product
</cell>
<cell>
# Test your code
print(tuple_product((1, 2, 3, 4, 5)))
</cell>
<text>
Exercise
Write a function that returns a tuple where each element is the largest of the element