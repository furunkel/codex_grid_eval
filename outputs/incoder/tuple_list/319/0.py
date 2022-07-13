
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest third value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[2])[11]

# Test Cases
print(tuple_extract(lst))
print(tuple_extract(lst2))
print(tuple_extract(lst3))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with the first two elements of the list reversed.


</text>
<cell>
def reverse_first_two(lst):
    """
    Given a list of tuples, write a function that returns the first two elements of the list reversed.
    """
    
    # Your code here
    
    return lst[::-1][:2]

# Test Cases
print(reverse_first_two(lst))
print(reverse_first_two(lst2))
print(reverse_first_two(lst3))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with the first three elements of the list reversed.


</text>
<cell>
def reverse_first_three(lst):
    """
    Given a list of tuples, write a function that returns the first three elements of the list reversed.
    """
    
    # Your code here
    
    return lst[::-1][:3]

# Test Cases
print(reverse_first_three(lst))
print(reverse_first_three(lst2))
print(reverse_first_three(lst3))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with the first four elements of the list reversed.


</text>
<cell>
def reverse_first_four(lst):
    """
    Given a list of tuples, write a function that returns the first four elements of the list reversed.
    """
    
    # Your code here
    
    return lst[::-1][:4]

# Test Cases
print(reverse_first_four(lst))
print(reverse_first_four(lst2))
print(reverse_first_four(lst3))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with the first five elements of the list reversed.


</text>
<cell>
def reverse_first_five(lst):
    """
    Given a list of tuples, write a function that returns the first five elements of the list reversed.
    """
    
    # Your code here
    
    return lst[::-1][:5]

# Test Cases
print(reverse_first_five(lst))
print(reverse_first_five(lst2))
print(reverse_first_five(lst3))
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a list with the first six elements of the list reversed.


</text>
<cell>
def reverse_first_six(lst):
