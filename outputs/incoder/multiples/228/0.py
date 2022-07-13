
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 3 or 5 below 197.
    """    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

# Problem 3
def fibonacci():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    Find the sum of all the even Fibonacci numbers below two million.
    """
    sum = 0
    a, b = 1, 2
    while b < 2000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 4
def fibonacci_sum():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even values.
    """
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
    return sum

# Problem 5
def fibonacci_sum_with_memoization():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even values.
    """
    memo = {}
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
            if b not in memo:
                memo[b] = 1
            else:
                memo[b] += 1
    return sum

# Problem 6
def fibonacci_sum_with_memoization_2():
    """
    By starting with 1 and 2, the first 10 numbers in the Fibonacci sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even values.
    """
    memo = {}
    a, b = 1, 2
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            sum += b
            if b not in memo:
                memo[b] = 1
            else:
                memo[b] += 1
    return sum

# Problem 7