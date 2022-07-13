
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The sum of these multiples is 37.
    Return the sum of all the multiples of 5, 3 or 2 below 124.
    """    
    return sum([i for i in range(1, 125) if i%5==0 or i%3==0 or i%2==0])

# Problem 3
def fibonacci():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    return sum([i for i in range(1, 6) if i%2==0])

# Problem 4
def fibonacci_sum():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    return sum([i for i in range(1, 6) if i%2==0 and i%3==0])

# Problem 5
def fibonacci_sum_with_condition():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    return sum([i for i in range(1, 6) if i%2==0 and i%3==0 and i%5==0])

# Problem 6
def fibonacci_sum_with_condition2():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    return sum([i for i in range(1, 6) if i%2==0 and i%3==0 and i%5==0 and i%7==0])

# Problem 7
def fibonacci_sum_with_condition3():
    """
    By listing the first six numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    We get 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    return sum([i for i in range(1, 6) if i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%9==