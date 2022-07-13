
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 197.
    """    
    
    multiples = []
    
    for n in range(2, int(math.sqrt(197)) + 1):
        if n % 5 == 0 and n % 7 == 0 and n % 9 == 0:
            multiples.append(n)
            
    return multiples 

print(multiples())
</cell>
<text>
Great! Now you know how to find the products of all the multiples of 3 or 5 below a certain number. Let's find all the multiples of 5 below 1000.


</text>
<cell>
def fives_under_1000():
    """
    Find all the multiples of 5 below 1000
    """
    
    multiples = []
    
    for n in range(2, int(math.sqrt(1000)) + 1):
        if n % 5 == 0:
            multiples.append(n)
            
    return multiples 

print(fives_under_1000())
</cell>
<text>
Oops! You might have expected 15 to be one of the numbers in this list. But that's not quite right. 15 is actually one of the multiples of 5, 7 or 9. If you want the multiples of 5 below 15, then you need to change the upper limit of the for loop to 14 and change the if statement to n % 5 == 0.


</text>
<cell>
def fives_under_1000():
    """
    Find all the multiples of 5 below 1000
    """
    
    multiples = []
    
    for n in range(2, 14):
        if n % 5 == 0:
            multiples.append(n)
            
    return multiples 

print(fives_under_1000())
</cell>
<text>
Great! Now you know how to find the products of all the multiples of 3 or 5 below a certain number. Let's find all the multiples of 7 below 1000.


</text>
<cell>
def sevens_under_1000():
    """
    Find all the multiples of 7 below 1000
    """
    
    multiples = []
    
    for n in range(2, int(math.sqrt(1000)) + 1):
        if n % 7 == 0:
            multiples.append(n)
            
    return multiples 

print(sevens_under_1000())
</cell>
<text>
Oops! You might have expected 29 to be one of the numbers in this list. But that's not quite right. 29 is actually one of the multiples of 7, 8 or 9.

If you want the multiples of 7 below 29, then you need to change the upper limit of the for loop to 28 and change the if statement to n % 7 == 0.


</text>
<cell>
def sevens_under_1000():
    """
    Find all the multiples of 7 below 1000
    """
    
    multiples = []
    
    for n in range(2, 28):
        if n % 7 == 0:
            multiples.append(n)
            
    return multiples 

print(sevens_under_