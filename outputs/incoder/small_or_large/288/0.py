
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < 0:
        return "mouse"
    elif n > 0:
        return "large"
    else:
        return None


# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ______________________________________________________________________________
# Problem 6

def fibonacci_iterative(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a


# ______________________________________________________________________________
# Problem 7

def lucky_number(n):
    """
    Starting with 1 and increasing by 1 on each step, return the sum of the numbers which are relatively prime to n.
    """
    sum = 0
    factor = 2
    while factor < n:
        if n % factor == 0:
            sum += factor
        factor += 1
    return sum


# ______________________________________________________________________________
# Problem 8

def fibonacci_python(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    if n < 2:
        return n
    else:
        return fibonacci_python(n - 1) + fibonacci_python(n - 2)


# ______________________________________________________________________________
# Problem 9

def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence. Fibonacci numbers are defined by the recurrence Tn = Tn−1 + Tn−2, where T0 = 1 and T1 = 1.
    """
    memo = {}
    if n in memo:
        return memo[n]
    elif n < 2:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]


# ______________________________________________________________________________
# Problem 10

def fibonacci_memoization_python(n):