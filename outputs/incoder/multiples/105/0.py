
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 200.
    """    
    
    multiples = []
    
    for n in range(2, 200):
        if n % 2 == 0:
            multiples.append(n)
        if n % 9 == 0:
            multiples.append(n)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to get the product of a list of numbers. Next, write a function that takes in a list of numbers, and returns the product of the numbers in the list squared.


</text>
<cell>
def squarednumbers(numbers):
    """
    Given a list of numbers, return a new list containing the squared numbers. 
    """
    
    squarednumbers = []
    
    for number in numbers:
        squarednumbers.append(number**2)
        
    return squarednumbers
</cell>
<cell>
squarednumbers([1, 2, 3, 4])
</cell>
<text>
Problem 2b
Square all the numbers between 1 and 1000 that are multiples of 3 or 5.


</text>
<cell>
def squaresbetween3and5(numbers):
    """
    Given a list of numbers, return a new list containing the squared numbers. 
    """
    
    squarednumbers = []
    
    for number in numbers:
        if number % 3 == 0:
            squarednumbers.append(number**2)
        if number % 5 == 0:
            squarednumbers.append(number**2)
            
    return squarednumbers
</cell>
<cell>
squaresbetween3and5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
</cell>
<text>
Problem 2c
Square all the numbers between 1 and 1000 that are multiples of 3 or 5, and also return the sum of all the numbers that are multiples of 3 or 5. 


</text>
<cell>
def squaresbetween3and5andsum(numbers):
    """
    Given a list of numbers, return a new list containing the squared numbers. 
    """
    
    squarednumbers = []
    
    for number in numbers:
        if number % 3 == 0:
            squarednumbers.append(