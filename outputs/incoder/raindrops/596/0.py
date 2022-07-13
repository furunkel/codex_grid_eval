
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Buzz".
    39 has both 13 and 3 as factors, but not 5, so the result would be "PlingPlang".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    factors = []
    for n in range(1, num + 1):
        if num % n == 0:
            factors.append(n)
    if len(factors) == 0:
        return str(num)
    elif len(factors) == 1:
        return "Buzz" if num in factors else "Pling" if num in factors else "Plang" if num in factors else "2"
    else:
        return "PlingPlang" if num in factors else "Buzz" if num in factors else "Pling" if num in factors else "Plang" if num in factors else "2"


# In[13]:


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
    10 has 3 as a factor, but not 5 or 7, so the result would be "Fizz".
    39 has both 3 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    factors = []
    for n in range(1, num + 1):
        if num % n == 0:
            factors.append(n)
    if len(factors) == 0:
        return str(num)
    elif len(factors) == 1:
        return "Fizz" if num in factors else "Buzz" if num in factors else "FizzBuzz" if num in factors else "2"
    else:
        return "FizzBuzz" if num in factors else "Fizz" if num in factors else "Buzz" if num in factors else "FizzBuzz" if num in factors else "2"


# In[14]:


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbu