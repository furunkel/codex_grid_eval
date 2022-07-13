
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    2
    """
    if n%11==0 and n%13==0:
        return 1
    elif n%11==0:
        return 2
    elif n%13==0:
        return 3
    else:
        return 0
</cell>
<cell>
fizz_buzz(50)
</cell>
<text>
Exercise 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list. For example, square_sum([1, 2, 3]) should return [1, 4, 9].

Hint: You can use a for loop to iterate through the list.


</text>
<cell>
def square_sum(lst):
    """Return a list where each element is the sum of the squares of the elements in the original list."""
    
    squares = []
    
    for num in lst:
        squares.append(num**2)
    
    return squares
</cell>
<cell>
square_sum([1, 2, 3])
</cell>
<text>
Exercise 4
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list except for those that are divisible by 3.

For example, square_sum_ex([2, 5, 3, 6, 9, 10, 12]) should return [4, 9, 12].

Hint: You can use a for loop to iterate through the list.


</text>
<cell>
def square_sum_ex(lst):
    """Return a list where each element is the sum of the squares of the elements in the original list except for those that are divisible by 3."""
    
    squares = []
    
    for num in lst:
        if num%3 == 0:
            squares.append(num)
        else:
            squares.append(num**2)
    
    return squares
</cell>
<cell>
square_sum_ex([2, 5, 3, 6, 9, 10, 12])
</cell>
<text>
Exercise 5
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list except for those that are divisible by 5 and 3.

For example, square_sum_ex([2, 5, 3, 6, 9, 10, 12]) should return [9, 12].

Hint: You can use a for loop to iterate through the list.


</text>
<cell>
def square_sum_ex(lst):
    """Return a list where each element is the sum of the squares of the elements in the original list except for those that are divisible by 5 and 3."""
    
    squares = []
    
    for num in lst:
        if num%5 == 0 and num%3 == 0:
            squares.append(num)
        else:
            squares.append(num**2)
    
    return squares
