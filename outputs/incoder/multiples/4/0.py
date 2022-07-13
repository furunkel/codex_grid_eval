
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 197.
    """    
    sum = 0
    for i in range(1, 201):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

def fibonacci():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return True
    return False

def fibonacci_sum():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return sum
    return False

def fibonacci_sum_2():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return sum
    return False

def fibonacci_sum_3():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return sum
    return False

def fibonacci_sum_4():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return sum
    return False

def fibonacci_sum_5():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or False.
    """
    sum = 0
    a, b = 0, 1
    for i in range(0, 201):
        sum += a
        a, b = b, a + b
        if sum == 55:
            return sum
    return False

def fibonacci_sum_6():
    """
    We list the Fibonacci numbers and see if the sum of the numbers is 55 or not. Return True or 