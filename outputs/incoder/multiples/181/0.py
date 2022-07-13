
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 5, 3 or 2 below 1000.
    """    
    return sum([i for i in range(1, 1000) if i%5==0 or i%3==0 or i%2==0])

#Problem 8
def fibonacci(n):
    """
    Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465 
    """
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Problem 9
def fibonacci_iterative(n):
    """
    Using a recursive function and memoization, fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465 
    """
    memo = {}
    if n<2:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fibonacci_iterative(n-1) + fibonacci_iterative(n-2)
            return memo[n]

#Problem 10
def fibonacci_memo(n):
    """
    Using a recursive function and memoization, fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465 
    """
    if n<2:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
            return memo[n]

#Problem 11
def fibonacci_memo_iterative