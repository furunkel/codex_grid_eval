
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of eleven (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both eleven and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

# Now let's test our function
print(fizzbuzz(15))
print(fizzbuzz(10))
print(fizzbuzz(5))
print(fizzbuzz(1))
print(fizzbuzz(15))
print(fizzbuzz(10))
print(fizzbuzz(5))
print(fizzbuzz(1))
</cell>
<text>
Exercise: Write a function that takes a list as input and returns a list where each element is the product of all the numbers in the list. For example, if the input list contains [2, 3, 4], the output should be [2, 6, 24].


</text>
<cell>
def products(lst):
    """
    Given a list as input, return a list where each element is the product of all the numbers in the list.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your function here
products([2, 3, 4])
</cell>
<text>
Exercise: Write a function that takes a list and returns a list where each element is the sum of the numbers in the list. For example, if the input list contains [2, 3, 4], the output should be [5, 7, 9].


</text>
<cell>
def sums(lst):
    """
    Given a list as input, return a list where each element is the sum of the numbers in the list.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your function here
sums([2, 3, 4])
</cell>
<text>
Exercise: Write a function that takes a list and returns a list where each element is the product of the numbers in the list. For example, if the input list contains [2, 3, 4], the output should be [24, 12, 24].


</text>
<cell>
def products(lst):
    """
    Given a list as input, return a list where each element is the product of the numbers in the list.
    """
    
    # Your code here
    
    return lst
</cell>
<cell>
# Test your function here
products([2, 3, 4])
</cell>
<text>
Exercise: Write a function that takes a list and returns a list where each element is the sum of the squares of the numbers in the list. For example, if the input list contains [2, 3, 4], the output should be [9, 27, 64].


</text>
<cell>
def squares(lst):
    """
    Given a list as input, return a list where each element 