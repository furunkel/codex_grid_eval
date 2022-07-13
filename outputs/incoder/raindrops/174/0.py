
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num % 3 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Pling"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 5
def fibonacci(num):
    """
    Your task is to convert a number into a string that contains the Fibonacci sequence of the given number.
    For example, the number 13 would return "13".
    The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597.
    Each new term in the sequence is the sum of the previous two terms.
    For example, when n is 13, the first two terms are 1 and 1, and the sum is 1 + 1 = 2.
    Therefore, the sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597.
    """
    fib = [0, 1]
    fib.append(fib[0] + fib[1])
    for i in range(2, num + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# Problem 6
def fibonacci_iterative(num):
    """
    Your task is to convert a number into a string that contains the Fibonacci sequence of the given number.
    For example, the number 13 would return "13".
    The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597.
    Each new term in the sequence is the sum of the previous two terms.
    For example, when n is 13, the first two terms are 1 and 1, and the sum is 1 + 1 = 2.
    Therefore, the sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597.
    """
    fib = [0, 1]
    fib.append(fib[0] + fib[1])
    for i in range(2, num + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# Problem 7
def fibonacci_memo(num):
    """
    Your task is to convert a number into a string that contains the Fibonacci sequence of the given number.
    For example, the number 13 would return "13".
    The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597.
    Each new term in the sequence is the sum of the previous two terms.
    For example, when n is 13, the first two terms are 1 and 1, and the sum is 