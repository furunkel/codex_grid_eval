
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The product of these multiples is 3225600.
    Return the product of all the multiples of 2 or 5 below 200.
    """    
    
    multiples = []
    
    for n in range(2, 200):
        if n % 2 == 0 or n % 5 == 0:
            multiples.append(n)
            
    return multiples 
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to find the products of all the multiples of 2 through 200.

Task: Can you find the sum of all the multiples of 2 through 200?


</text>
<cell>
def sum_of_multiples():
    """
    Sum of all the multiples of 2 through 200.
    """
    
    sum_of_multiples = 0
    
    for n in range(2, 200):
        if n % 2 == 0:
            sum_of_multiples += n
            
    return sum_of_multiples 
</cell>
<cell>
sum_of_multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 2 through 200.

Task: Can you find the sum of all the multiples of 3 through 200?


</text>
<cell>
def sum_of_multiples():
    """
    Sum of all the multiples of 3 through 200.
    """
    
    sum_of_multiples = 0
    
    for n in range(3, 200):
        if n % 3 == 0:
            sum_of_multiples += n
            
    return sum_of_multiples 
</cell>
<cell>
sum_of_multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 3 through 200.

Task: Can you find the sum of all the multiples of 4 through 200?


</text>
<cell>
def sum_of_multiples():
    """
    Sum of all the multiples of 4 through 200.
    """
    
    sum_of_multiples = 0
    
    for n in range(4, 200):
        if n % 4 == 0:
            sum_of_multiples += n
            
    return sum_of_multiples 
</cell>
<cell>
sum_of_multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 4 through 200.

Task: Can you find the sum of all the multiples of 5 through 200?


</text>
<cell>
def sum_of_multiples():
    """
    Sum of all the multiples of 5 through 200.
    """
    
    sum_of_multiples = 0
    
    for n in range(5, 200):
        if n % 5 == 0:
            sum_of_multiples += n
            
    return sum_of_multiples 
</cell>
<cell>
sum_of_multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 5 through 