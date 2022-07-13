
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 1000.
    """    
    sum = 0
    for i in range(1, 1001):
        if i % 5 == 0:
            sum += i
    return sum

def fibonacci():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    for i in range(10):
        c = a + b
        a = b
        b = c
        print(c)

def fibonacci_sum():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    for i in range(10):
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_while():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    while a < 10:
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_for():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    for i in range(10):
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_while2():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    while a < 10:
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_for2():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    for i in range(10):
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_while3():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the Fibonacci sequence. 
    """
    a = 0
    b = 1
    sum = 0
    while a < 10:
        c = a + b
        a = b
        b = c
        sum += c
        print(sum)

def fibonacci_sum_with_for3():
    """
    Using two variables, a and b, we can compute and print the first ten terms of the 