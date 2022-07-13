
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "PlingBuzz".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num < 1:
        return "Not a number"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num % 2 == 0:
        if num % 13 == 0:
            return "Pling"
        if num % 3 == 0:
            return "Buzz"
        if num % 5 == 0:
            return "Plong"
    if num % 13 == 0:
        return "PlingBuzz"
    if num % 3 == 0:
        return "PlingBuzz"
    if num % 5 == 0:
        return "PlingBuzz"
    return "PlingBuzz"


# In[15]:


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append the word 'Fizz' to the result, and for multiples of five (buzz), you append the word 'Buzz' to the result.
    You do not need to worry about numbers that do not divide evenly into another number, as fizzbuzz does not need to handle those cases. For example, fizzbuzz(4) returns 'FizzBuzz'.
    
    Examples:
    1 returns "1"
    2 returns "2"
    3 returns "Fizz"
    4 returns "FizzBuzz"
    5 returns "Buzz"
    10 returns "FizzBuzz"
    20 returns "BuzzFizz"
    100 returns "FizzBuzz"
    300 returns "FizzBuzz"
    500 returns "BuzzFizz"
    1000 returns "FizzBuzz"
    10000 returns "BuzzFizzBuzz"
    """
    if num < 1:
        return "Not a number"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 13 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "FizzBuzz"
    return "FizzBuzz"


# In[16]:


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append the word 'Fizz' to the result, and for multiples of five (buzz), you append the word 'Buzz' to the result.
    