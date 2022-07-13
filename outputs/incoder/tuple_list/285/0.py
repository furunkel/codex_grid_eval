
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest last value.
    """
    return max(lst)[2]

# Test your function
print(some_func([(7, 8, 9), (4, 5, 6), (10, 11, 12)]))
</cell>
<text>
Great job!

</text>
<text>
Exercise 3
Write a function that takes a list and returns a new list with all the even numbers in that list.


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the even numbers.
    """
    return [x for x in lst if x % 2 == 0]

# Test your function
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Great job!

</text>
<text>
Exercise 4
Write a function that takes a list and returns a new list with all the odd numbers in that list.


</text>
<cell>
def odd_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the odd numbers.
    """
    return [x for x in lst if x % 2 != 0]

# Test your function
print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Great job!

</text>
<text>
Exercise 5
Write a function that takes a list and returns a new list with all the numbers that are on the first position of that list.


</text>
<cell>
def first_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the numbers on the first position.
    """
    return [x for x in lst if x == lst[0]]

# Test your function
print(first_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Great job!

</text>
<text>
Exercise 6
Write a function that takes a list and returns a new list with all the numbers that are on the last position of that list.


</text>
<cell>
def last_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the numbers on the last position.
    """
    return [x for x in lst if x == lst[-1]]

# Test your function
print(last_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
</cell>
<text>
Great job!

</text>
<text>
Exercise 7
Write a function that takes a list and returns a new list with all the numbers that are in the list but are not on the first or last position.


</text>
<cell>
def numbers_in_list_not_on_first_or_last_position(lst):
    """
    Given a list of numbers, return a new list containing only the numbers that are in the list but are not on the first or last position.
    """
    return [x for x in lst if x not in first_numbers(lst) or x not in last_numbers(lst)]

# Test your function
