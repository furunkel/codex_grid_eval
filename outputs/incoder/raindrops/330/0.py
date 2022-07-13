
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 11, 3, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'Buzz'
    elif num == 11:
        return 'Pling'
    elif num == 12:
        return 'Plong'
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if len(factors) == 0:
            return str(num)
        elif len(factors) == 1:
            return str(factors[0])
        else:
            factors.sort()
            factors.reverse()
            factors.insert(0, str(num))
            factors.append('Plong')
            factors.append('Pling')
            factors.append('Buzz')
            return ''.join(factors)

# Cell
def fibonacci(n):
    """
    Your task is to implement a function that returns the nth fibonacci number.

    Fibonacci numbers are the numbers in the Fibonacci sequence starting with 0, 1, 1, 2, 3, 5, 8, 13, ...
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time they are used.
    They are the first two numbers in the Fibonacci sequence and they grow by two each time 