
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 200.
    """    
    sum = 0
    for i in range(1, 200):
        if i % 5 == 0 or i % 3 == 0 or i % 2 == 0:
            sum += i
    return sum

# Problem 5
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269,
    2178309, 3524578,
    5702887, 9227465.
    Find the sum of all the even-valued terms in the Fibonacci sequence to equal a specific integer n.
    """
    sum = 0
    if n <= 1:
        return n
    else:
        for i in range(1, n):
            if i % 2 == 0:
                sum += i
        return sum

# Problem 6
def fibonacci_sum(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269,
    2178309, 3524578,
    5702887, 9227465.
    Find the sum of all the even-valued terms in the Fibonacci sequence to equal a specific integer n.
    """
    sum = 0
    if n <= 1:
        return n
    else:
        for i in range(1, n):
            if i % 2 == 0:
                sum += i
        return sum

# Problem 7
def fibonacci_sum_of_divisors(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269,
    2178309, 3524578,
    5702887, 9227465.
    Find the sum of all the even-valued terms in the Fibonacci sequence to equal 