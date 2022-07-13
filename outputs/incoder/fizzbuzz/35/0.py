
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of five (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both five and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    else:
        return num

# print fizzbuzz(100)
</cell>
<text>
Exercise 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list. For example, if the list is [1,2,3,4,5], the function should return [1,4,9,16,25]. Make sure your function works with any list whose elements are all integers.


</text>
<cell>
def square_of_list(my_list):
    """
    Takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list.
    For example, if the list is [1,2,3,4,5], the function should return [1,4,9,16,25].
    Make sure your function works with any list whose elements are all integers.
    """
    
    squares = []
    
    for num in my_list:
        squares.append(num**2)
    
    return squares

# print square_of_list([1,2,3,4,5])
</cell>
<text>
Exercise 8
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list. For example, if the list is [1,2,3,4,5], the function should return [1,4,9,16,25]. Make sure your function works with any list whose elements are all integers.


</text>
<cell>
def square_of_list(my_list):
    """
    Takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list.
    For example, if the list is [1,2,3,4,5], the function should return [1,4,9,16,25].
    Make sure your function works with any list whose elements are all integers.
    """
    
    squares = []
    
    for num in my_list:
        squares.append(num**2)
    
    return squares

# print square_of_list([1,2,3,4,5])
</cell>
<text>
Exercise 9
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list. For example, if the list is [1,2,3,4,5], the function should return [1,4,9,16,25]. Make sure your function works with any list whose elements are all integers.


</text>
<cell>
def square_of_list(my_list):
    """
    Takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the list.
    For example, if the list is [1,2,3,4,5], the 