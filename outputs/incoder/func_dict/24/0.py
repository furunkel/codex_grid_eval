
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i**2) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    """
    
    dictionary = {}
    
    for i in range(1, n+1):
        dictionary[i] = i**2
    
    return dictionary
</cell>
<cell>
# Test your code
n = 4
dictionary = generate_dict(n)
assert dictionary == {1: 1, 2: 4, 3: 9, 4: 16}
</cell>
<text>
Write a program to find the sum of the numbers between 1 and n inclusive.

</text>
<cell>
def sum_of_numbers(n):
    """
    With a given integral number n, write a program to find the sum of the numbers between 1 and n inclusive.
    
    """
    
    sum = 0
    
    for i in range(1, n+1):
        sum += i
    
    return sum
</cell>
<cell>
# Test your code
n = 4
assert sum_of_numbers(n) == 10
</cell>
<text>
Write a program to find the product of the numbers between 1 and n inclusive.

</text>
<cell>
def product_of_numbers(n):
    """
    With a given integral number n, write a program to find the product of the numbers between 1 and n inclusive.
    
    """
    
    product = 1
    
    for i in range(1, n+1):
        product *= i
    
    return product
</cell>
<cell>
# Test your code
n = 4
assert product_of_numbers(n) == 24
</cell>
<text>
Write a program to find the remainder when dividing n by m.

</text>
<cell>
def remainder(n, m):
    """
    With a given integral number n and another integral number m, write a program to find the remainder when dividing n by m.
    
    """
    
    remainder = 0
    
    for i in range(1, n+1):
        remainder += i % m
    
    return remainder
</cell>
<cell>
# Test your code
n = 4
m = 2
assert remainder(n, m) == 2
</cell>
<text>
Write a program to find the factorial of a given number.

</text>
<cell>
def factorial(n):
    """
    With a given integral number n, write a program to find the factorial of a given number.
    
    """
    
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
    
    return factorial
</cell>
<cell>
# Test your code
n = 4
assert factorial(n) == 24
</cell>
<text>
Write a program to find the sum of all even integers less than or equal to n.

</text>