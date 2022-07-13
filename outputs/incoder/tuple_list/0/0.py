
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(lst)[1]

# Test your function
print(extract_value(lst))
</cell>
<text>
Great job!

</text>
<text>
Exercise - Write a function that returns a list of all the even numbers from an input list. Call the function with lst = [1, 3, 5, 7, 9]. Make sure you only use loops, no list comprehensions!


</text>
<cell>
# UNQ_C8 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: even_numbers
def even_numbers(lst):
    """
    Given a list of numbers, return a list of all the even numbers.
    
    Examples:
        even_numbers([1, 5, 7, 9]) should return [1, 3, 5]
        even_numbers([1, 2, 3, 4]) should return [2, 4]
    """
    even_numbers = []
    
    ### START CODE HERE ###
    
    even_numbers = [num for num in lst if num % 2 == 0]
    
    ### END CODE HERE ###
    
    return even_numbers

# Test your function
print(even_numbers([1, 5, 7, 9]))
print(even_numbers([1, 2, 3, 4]))
</cell>
<text>
Note
If you don't know what % is, read the explanation here.

If you feel stuck and need a hint, check out the solutions notebook.


</text>
<text>
Exercise - Write a function that returns a list of all the numbers from an input list up to and including the first number that is a multiple of 7. Call the function with lst = [1, 7, 3, 9, 5, 7] and 7. Make sure you only use loops, no list comprehensions!


</text>
<cell>
# UNQ_C9 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: mod_seven
def mod_seven(lst):
    """
    Given a list of numbers, return a list of all the numbers in the list that are
    divisible by 7.
    
    Examples:
        mod_seven([2, 7, 11, 13, 14]) should return [2, 7, 3]
        mod_seven([2, 3, 11, 7, 13]) should return [2, 3, 11]
        mod_seven([2, 7, 11, 13]) should return [2, 7, 3]
        mod_seven([2, 7, 11, 13, 14]) should return [2, 7, 3]
    """
    mod_seven = []
    
    ### START CODE HERE ###
    
    mod_seven = [num for num in lst if num % 7 == 0]
    
    ### END CODE HERE ###
    
