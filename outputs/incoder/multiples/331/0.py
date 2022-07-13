
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 9 below 500.
    """    
    return prod(filter(lambda x: x%2 == 0 or x%9 == 0, range(2,500)))
</cell>
<cell>
multiples()
</cell>
<text>
Write a function that returns the product of an array of numbers and a fixed number. For example, product_of_array_and_number([1,2,3,4], 2) should return 24.


</text>
<cell>
def product_of_array_and_number(array, number):
    """
    Takes in an array and an integer, and returns the product of the array and the integer.
    """
    return reduce(lambda x, y: x*y, array)
</cell>
<cell>
product_of_array_and_number([1,2,3,4], 2)
</cell>
<text>
Write a function that checks whether a number is in a given array or not. For example, is_in_array([1,2,3,4], 2) should return True. is_in_array([1,2,3,4], 7) should return False.


</text>
<cell>
def is_in_array(array, number):
    """
    Takes in an array and an integer, and returns True if the integer is present in the array, False otherwise.
    """
    return number in array
</cell>
<cell>
is_in_array([1,2,3,4], 2)
</cell>
<text>
Write a Python program to find the sum of all elements in a given array of numbers.


</text>
<cell>
def sum_of_elements(array):
    """
    Takes in an array of numbers and returns the sum of all the elements in the array.
    """
    return sum(array)
</cell>
<cell>
sum_of_elements([1,2,3,4])
</cell>
<text>
Write a Python program to find the product of all elements in a given array of numbers.


</text>
<cell>
def product_of_elements(array):
    """
    Takes in an array of numbers and returns the product of all the elements in the array.
    """
    return reduce(lambda x, y: x*y, array)
</cell>
<cell>
product_of_elements([1,2,3,4])
</cell>
<text>
Write a Python program to find the largest number in an array.


</text>
<cell>
def largest_number(array):
    """
    Takes in an array of numbers and returns the largest number in the array.
    """
    return max(array)
</cell>
<cell>
largest_number([1,2,3,4])
</cell>
<text>
Write a Python program to find the smallest number in an array.


</text>
<cell>
def smallest_number(array):
    """
    Takes in an array of numbers and returns the smallest number in the array.
    """
    return min(array)
</cell>
<cell>
smallest_number([1,2,3,4])
</cell>
<text>
Write a Python program to find the number of positive numbers in a given array of numbers.