
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 5, 3 or 2 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            sum += i
    return sum

# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    
    # Get the DATA entered by the USER
    
    # Analyse the DATA
    
    # Generate the RESULTS
    
    # Presentation of the RESULTS in a neat FORM
    
    # END MAIN PROGRAM

    


if __name__ == "__main__":
    main()



</cell>
<text>
Exercise 1.10
Write a Python program to find the sum of all the numbers from 1 to 100 that are divisible by 7 and 5 using the following formula:

$ \sum_{i=1}^{100} i^2 $

The program should use an "if" statement to determine if the number is a multiple of 7 or 5.


</text>
<cell>
# Definition of FUNCTIONS


# START Definition of FUNCTIONS

def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 7, 5 we get 7, 14, 21, ... 100. The sum of these multiples is 170.
    Return the sum of all the multiples of 7, 5 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 7 == 0 and i % 5 == 0:
            sum += i
    return sum

# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    
    # Get the DATA entered by the USER
    
    # Analyse the DATA
    
    # Generate the RESULTS
    
    # Presentation of the RESULTS in a neat FORM
    
    # END MAIN PROGRAM

    


if __name__ == "__main__":
    main()



</cell>
<text>
Exercise 1.11
Write a Python program to find the sum of all the numbers from 1 to 100 that are divisible by 7 and 5 using the following formula:

$ \sum_{i=1}^{100} i^2 $

The program should use an "if" statement to determine if the number is a multiple of 7 or 5.


</text>
<cell>
# Definition of FUNCTIONS


# START Definition of FUNCTIONS

def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 7, 5 we get 7, 14, 21, ... 100. The sum of these multiples is 170.
    Return the sum of all the multiples of 7, 5 below 100.
    """    
    
    sum = 0
    for i in range(1, 101):
        if i % 7 == 0 and i % 5 == 0:
            sum += i
    return sum