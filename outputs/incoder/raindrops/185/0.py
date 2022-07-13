
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Buzz".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    
    if num % 3 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Pling"
    elif num % 7 == 0:
        return "Buzz"
    else:
        return str(num)

#test
print(raindrops(14))
print(raindrops(33))
print(raindrops(2))
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the recurrence relation:

Fn = F(n-1) + F(n-2), where F(0) = 1 and F(1) = 1. 
For example, F(3) = F(2) + F(1) = F(1) + F(0) = 1 + 1 = 2. 
By starting with F(0) = 1 and F(1) = 1, the first 12 terms will be:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci(n):
    """
    Your task is to compute the sum of the even values of the Fibonacci sequence
    up to and including n.
    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#test
print(fibonacci(4))
print(fibonacci(12))
print(fibonacci(20))
</cell>
<text>
Problem 4
The Fibonacci sequence is defined by the recurrence relation:

Fn = F(n-1) + F(n-2), where F(0) = 1 and F(1) = 1. 
For example, F(3) = F(2) + F(1) = F(1) + F(0) = 1 + 1 = 2. 
By starting with F(0) = 1 and F(1) = 1, the first 12 terms will be:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


</text>
<cell>
def fibonacci(n):
    """
    Your task is to compute the sum of the even values of the Fibonacci sequence
    up to and including n.
    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#test
print(fibonacci(4))
print(fibonacci(12))
print(fibonacci(20))
</cell