
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 9, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 9 below 197.
    """    
    
    multiples = []
    
    for i in range(1, 20):
        if i % 2 == 0 or i % 9 == 0:
            multiples.append(i)
    
    return multiples[len(multiples) - 1]
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to check if a number is even or odd, and how to list the multiples of 2 and 9.

</text>
<text>
Problem 3
Write a function that returns the product of all the numbers in the list below:

numbers = [1, 2, 3, 4, 5]

</text>
<cell>
def products(numbers):
    """
    Returns the product of all the numbers in the list below:
    
    numbers = [1, 2, 3, 4, 5]
    """
    
    product = 1
    
    for i in numbers:
        product *= i
        
    return product
</cell>
<cell>
products([1, 2, 3, 4, 5])
</cell>
<text>
Great! Now you know how to find the product of a list of numbers.

</text>
<text>
Problem 4
Write a function that will print out a pattern based on the input n, for example, if the input is 5, it will print out a 5 x 5 grid.

   

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

