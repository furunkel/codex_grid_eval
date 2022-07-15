
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i * i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    1
    Then, the output should be:
    {1: 1}

    """
    
    dict = {}
    for i in range(1, n + 1):
        dict[i] = i * i
    return dict


# Write a Python program to find the largest number whose product of digits is equal to the given number.
def largest_product(n):
    """
    With a given integral number n, write a program to find the largest number whose product of digits is equal to n.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    100
    
    """
    
    product = 1
    
    for i in range(1, n):
        product *= int(str(n)[i])
    
    return product


# Write a Python program to find the smallest number whose product of digits is equal to the given number.
def smallest_product(n):
    """
    With a given integral number n, write a program to find the smallest number whose product of digits is equal to n.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    1
    
    """
    
    product = 1
    
    for i in range(1, n):
        product *= int(str(n)[i])
    
    return product


# Write a Python program to find the largest number whose product of digits is less than or equal to the given number.
def largest_product_less_than(n):
    """
    With a given integral number n, write a program to find the largest number whose product of digits is less than or equal to n.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    100
    
    """
    
    product = 1
    
    for i in range(1, n):
        product *= int(str(n)[i])
    
    return product


# Write a Python program to find the smallest number whose product of digits is less than or equal to the given number.
def smallest_product_less_than(n):
    """
    With a given integral number n, write a program to find the smallest number whose product of digits is less than or equal to n.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    1
    
    """
    
    product = 1
    
    for i in range(1, n):
        product *= int(str(n)[i])
    
    return product


# Write a Python program to find the largest number whose product of digits is greater than or equal to the given number.
def largest_product_greater_than(n):
    """
    With a given integral number n, write a program to find the largest number whose product of digits is greater than or equal to n.
    
    Suppose the following input is supplied to the function:
    100
    Then, the output should be:
    100
    
    """
    