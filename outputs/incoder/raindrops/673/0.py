
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plang".
    143 has both 13 and 11 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    factors = []
    number = num
    
    while number != 0:
        if number % 13 == 0:
            factors.append('Fizz')
        elif number % 11 == 0:
            factors.append('Buzz')
        elif number % 7 == 0:
            factors.append('Plang')
        else:
            factors.append(str(number))
        number //= 10
    
    return ''.join(factors)


# In[14]:


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    3 has 3 as a factor, so the result would be "Fizz".
    5 has 5 as a factor, so the result would be "Buzz".
    7 has 7 as a factor, so the result would be "FizzBuzz".
    9 is not factored by 3, 5, or 7, so the result would be "9".
    """
    factors = []
    number = num
    
    while number != 0:
        if number % 3 == 0:
            factors.append('Fizz')
        elif number % 5 == 0:
            factors.append('Buzz')
        elif number % 7 == 0:
            factors.append('FizzBuzz')
        else:
            factors.append(str(number))
        number //= 10
    
    return ''.join(factors)


# In[15]:


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits 