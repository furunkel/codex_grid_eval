
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 5 below 124.
    """    
    
    multiples = []
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            multiples.append(n)
        elif n % 5 == 0:
            multiples.append(n)
    
    return multiples 
</cell>
<cell>
multiples()
</cell>
<cell>
def multiples_2(multiples):
    """
    Using a for loop, add all the multiples of 2 or 5 below 124.
    """
    
    total = 0
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            total += n
        elif n % 5 == 0:
            total += n
    
    return total
</cell>
<cell>
multiples_2(multiples())
</cell>
<cell>
def multiples_3(multiples):
    """
    Using a for loop, add all the multiples of 2 or 5 below 124.
    """
    
    total = 0
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            total += n
        elif n % 5 == 0:
            total += n
    
    return total
</cell>
<cell>
multiples_3(multiples())
</cell>
<cell>
def multiples_4(multiples):
    """
    Using a for loop, add all the multiples of 2 or 5 below 124.
    """
    
    total = 0
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            total += n
        elif n % 5 == 0:
            total += n
    
    return total
</cell>
<cell>
multiples_4(multiples())
</cell>
<cell>
def multiples_5(multiples):
    """
    Using a for loop, add all the multiples of 2 or 5 below 124.
    """
    
    total = 0
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            total += n
        elif n % 5 == 0:
            total += n
    
    return total
</cell>
<cell>
multiples_5(multiples())
</cell>
<cell>
def multiples_6(multiples):
    """
    Using a for loop, add all the multiples of 2 or 5 below 124.
    """
    
    total = 0
    
    for n in range(125, 1, -1):
        if n % 2 == 0:
            total += n
        elif n % 5 == 0:
            total += n
    
    return total
</cell>
<cell>
multiples_6(multiples())
</cell>
<cell>
def multiples_7(multiples):
    """
