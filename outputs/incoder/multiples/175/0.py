
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 5, 3 or 2 below 200.
    """    
    
    multiples = []
    for n in range(15):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            multiples.append(n)
    return multiples[:]

#=======================================================================================================================
# Problem 4
# Write a function that returns the sum of the squares of the first N integers (starting from 1).
#=======================================================================================================================
def sumOfSquares(N):
    """
    Sum of squares up to N
    """
    
    sum = 0
    for n in range(N):
        sum += n*n
    return sum

#=======================================================================================================================
# Problem 5
# Write a function that returns the sum of the first N integers (starting from 1) squared.
#=======================================================================================================================
def sumOfSquares(N):
    """
    Sum of squares up to N
    """
    
    sum = 0
    for n in range(N):
        sum += n*n
    return sum

#=======================================================================================================================
# Problem 6
# Write a function that returns the product of the integers 1 through N.
#=======================================================================================================================
def productOfNumbers(N):
    """
    Product of numbers 1 through N
    """
    
    product = 1
    for n in range(N):
        product *= n
    return product

#=======================================================================================================================
# Problem 7
# Write a function that returns the product of the integers 1 through N squared.
#=======================================================================================================================
def productOfNumbers(N):
    """
    Product of numbers 1 through N squared
    """
    
    product = 1
    for n in range(N):
        product *= n
    return product

#=======================================================================================================================
# Problem 8
# Write a function that accepts a string and returns the number of uppercase and lowercase letters.
#=======================================================================================================================
def countLetters(string):
    """
    Count uppercase and lowercase letters
    """
    
    upperCase = 0
    lowerCase = 0
    for letter in string:
        if letter.isupper():
            upperCase += 1
        elif letter.islower():
            lowerCase += 1
    return upperCase, lowerCase

#=======================================================================================================================
# Problem 9
# Write a function that accepts a string and returns the number of words in the string.
#=======================================================================================================================
def countWords(string):
    """
    Count words
    """
    
    count = 0
    for word in string.split():
        count += 1
    return count

#=======================================================================================================================
# Problem 10
# Write a function that accepts a string and returns the number of characters in the string.
#=======================================================================================================================
def countCharacters(string):
    """
    Count characters