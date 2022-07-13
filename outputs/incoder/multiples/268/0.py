
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 124.
    """    
    
    sum = 0
    for i in range(1, 125):
        if i % 2 == 0:
            sum += i
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Great! Now you know how to sum all the multiples of 2, 3 or 5 below 1000.


</text>
<text>
Problem 7
Write a function that computes the factorial of a number. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120


</text>
<cell>
def factorial(n):
    """
    Compute n!
    """
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))
</cell>
<text>
Problem 8
Write a function that checks whether a number is "happy". Happy(27) = True, Happy(-10) = False, Happy(0) = True, Happy(25) = False


</text>
<cell>
def happy(number):
    """
    Check to see if a number is "happy".
    """
    
    if number < 0:
        return False
    elif number == 0:
        return True
    elif number > 0 and number < 10:
        return True
    else:
        return False

print(happy(27))
print(happy(-10))
print(happy(0))
print(happy(25))
</cell>
<text>
Problem 9
Write a function that grabs the high number from an arithmetic progression. For example, the output of the high number for 4-7 would be 7 and the output for 9-10 would be 10. Make sure to handle negative numbers!


</text>
<cell>
def high_number(start, end):
    """
    Find the high number in an arithmetic progression.
    """
    
    high = start
    for i in range(start, end):
        if i > high:
            high = i
    return high

print(high_number(4, 7))
print(high_number(9, 10))
</cell>
<text>
Problem 10
Write a function that grabs the low number from an arithmetic progression. For example, the output of the low number for 4-7 would be 4 and the output for 9-10 would be 9.

Make sure to handle negative numbers!


</text>
<cell>
def low_number(start, end):
    """
    Find the low number in an arithmetic progression.
    """
    
    low = start
    for i in range(start, end):
        if i < low:
            low = i
    return low

print(low_number(4, 7))
print(low_number(9, 10))
</cell>
<text>
Problem 11
Write a function that checks whether a number is "happy". Happy(27) = True, 