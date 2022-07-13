
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst)[2]

# Test the function
print(extract_value([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the sum of the elements in the list.


</text>
<cell>
def sum_of_list(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    return sum(lst)

# Test the function
print(sum_of_list([1,2,3]))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the product of the elements in the list.


</text>
<cell>
def product_of_list(lst):
    """
    Given a list of numbers, return the product of the numbers in the list.
    """
    return prod(lst)

# Test the function
print(product_of_list([1,2,3]))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list.


</text>
<cell>
def count_elements(lst):
    """
    Given a list of numbers, return the number of elements in the list.
    """
    return len(lst)

# Test the function
print(count_elements([1,2,3]))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements that are greater than the value of the element in the list.


</text>
<cell>
def count_greater_than_element(lst):
    """
    Given a list of numbers, return the number of elements that are greater than the value of the element in the list.
    """
    return len([x for x in lst if x > lst[0]])

# Test the function
print(count_greater_than_element([1,2,3]))
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the number of elements that are less than the value of the element in the list.


</text>
<cell>
def count_less_than_element(lst):
    """
    Given a list of numbers, return the number of elements that are less than the value of the element in the list.
    """
    return len([x for x in lst if x < lst[0]])

# Test the function
print(count_less_than_element([1,2,3]))
</cell>
<text>
Problem 12
Write a function that takes a list as an argument and returns the number of elements that are equal to the value of the element in the list.


</text>
<cell>
def count_equal_to_element(lst):
    """
    Given a list of numbers, return the number of elements that are equal to the value of the element in the list.
    """
    return len([x for x in lst if x == lst[0]])

# Test the function
print(count_equal_to_element([1,2,3]))
</cell>
<text>
Problem 