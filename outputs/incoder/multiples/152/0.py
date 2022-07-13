
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The sum of these multiples is 61.
    Return the sum of all the multiples of 2 or 5 below 1000.
    """    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

def sum_of_divisors(n):
    """
    Sum of divisors of a number
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def sum_of_divisors_recursive(n):
    """
    Sum of divisors of a number using recursion
    """
    if n == 1:
        return 1
    else:
        return n + sum_of_divisors_recursive(n - 1)

def sum_of_divisors_iterative(n):
    """
    Sum of divisors of a number using iteration
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def sum_of_divisors_memoization(n):
    """
    Sum of divisors of a number using memoization
    """
    memo = {}
    def sum_of_divisors_helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        else:
            sum = n + sum_of_divisors_helper(n - 1)
            memo[n] = sum
            return sum
    return sum_of_divisors_helper(n)

def sum_of_divisors_memoization_iterative(n):
    """
    Sum of divisors of a number using memoization and iteration
    """
    memo = {}
    def sum_of_divisors_helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        else:
            sum = n + sum_of_divisors_helper(n - 1)
            memo[n] = sum
            return sum
    return sum_of_divisors_helper(n)

def sum_of_divisors_memoization_iterative_recursive(n):
    """
    Sum of divisors of a number using memoization and recursion
    """
    memo = {}
    def sum_of_divisors_helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        else:
            sum = n + sum_of_divisors_helper(n - 1)
            memo[n] = sum
            return sum
    return sum_of_divisors_helper(n)

def sum_of_divisors_memoization_iterative_recursive_iterative(n):
    """
    Sum of divisors of a number using memoization and recursion and iteration
    """
    memo = {}
    def sum_of_divisors_helper(n):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        else:
            sum = n + sum_of_divisors_helper(n - 1)
            memo[n] = sum
            return sum
    return sum_of_divisors_helper(n)

def sum_of_divisors_memoization_iterative_recur