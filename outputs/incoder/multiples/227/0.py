
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The product of these multiples is 3.
    Return the product of all the multiples of 3 or 5 below 124.
    """    
    
    multiples = []
    
    for i in range(124, 1, -1):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
            
    return multiples 
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to find the products of all the multiples of 3 or 5 below 1000.


</text>
<text>
Problem 9
The fibonacci sequence is defined by the formula:

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,...$

It can be defined recursively as:

$Fn = F{n-1} + F_{n-2}$

Where $F_{0} = 0$ and $F_{1} = 1$

Implement fibonacci function which calculates the nth number in the fibonacci sequence


</text>
<cell>
def fibonacci(n):
    """
    Calculates the nth number in the fibonacci sequence
    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
</cell>
<cell>
fibonacci(10)
</cell>
<text>
Problem 10
Write a function that takes in a mathematical expression and evaluates it. Mathematical expressions can include variables, arithmetic operators, and functions. For example, the below expression can be evaluated.

$$(x + 3)(x - 2)(2x - 1)(x^2 - 2x + 1)$$

The function definition should look like:

def evaluate_expression(expression):
    """
    Takes in a mathematical expression and evaluates it
    """
    # Your code here
    return value
Make sure you take in account that the expression could contain variables and functions
Make sure you take in account that the expression could contain variables and functions
Make sure you take in account that the expression could contain variables and functions


</text>
<cell>
def evaluate_expression(expression):
    """
    Takes in a mathematical expression and evaluates it
    """
    
    # Your code here
    return value
</cell>
<cell>
evaluate_expression('(x + 3)(x - 2)(2x - 1)(x^2 - 2x + 1)')
</cell>
<text>
Problem 11
Write a function that takes a mathematical expression and evaluates it. Mathematical expressions can include variables, arithmetic operators, and functions. For example, the below expression can be evaluated.

$$(x + 3)(x - 2)(2x - 1)(x^2 - 