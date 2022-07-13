
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    
    return max(lst)[1]

# Test your function
print(tuple_extract(lst))
</cell>
<text>
Expected output
4

</text>
<text>
Write a function that returns the first element of the tuple with the largest last value.


</text>
<cell>
def tuple_extract_first(lst):
    """
    Given a list of tuples, write a function that returns the first element of the tuple with the largest last value.
    """
    
    return max(lst)[0]

# Test your function
print(tuple_extract_first(lst))
</cell>
<text>
Expected output
2

</text>
<text>
Write a function that returns a list of all the negative numbers in an input list of integers.


</text>
<cell>
def negative_list(lst):
    """
    Given a list of integers, return a list of the negative numbers in that list.
    """
    
    return [num for num in lst if num < 0]

# Test your function
print(negative_list([-4, -2, 0, 2, 4]))
</cell>
<text>
Expected output
[-4, 0, 2]

</text>
<text>
Write a function that returns a list of all the positive numbers in an input list of integers.


</text>
<cell>
def positive_list(lst):
    """
    Given a list of integers, return a list of the positive numbers in that list.
    """
    
    return [num for num in lst if num > 0]

# Test your function
print(positive_list([-4, -2, 0, 2, 4]))
</cell>
<text>
Expected output
[-2, 0, 4]

</text>
<text>
Write a function that returns a list of all the even numbers in an input list of integers.


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of integers, return a list of the even numbers in that list.
    """
    
    return [num for num in lst if num % 2 == 0]

# Test your function
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Expected output
[2, 4, 6, 8]

</text>
<text>
Write a function that returns a list of all the odd numbers in an input list of integers.


</text>
<cell>
def odd_numbers(lst):
    """
    Given a list of integers, return a list of the odd numbers in that list.
    """
    
    return [num for num in lst if num % 2 != 0]

# Test your function
print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Expected output
[1, 3, 5, 7, 9]

</text>
<text>
Write a function that returns a list of all the numbers that are both even and odd in an input list of integers.


</text>
<