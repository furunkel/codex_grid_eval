
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The sum of these multiples is 61.
    Return the sum of all the multiples of 2 or 5 below 197.
    """    
    
    sum = 0
    for n in range(2, int(math.sqrt(197)) + 1):
        if n % 2 == 0:
            sum += n
        if n % 5 == 0:
            sum += n
    return sum

# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    
    # Get the DATA entered by the USER
    
    # Analyse the DATA
    
    # Generate the RESULT
    
    # DISPLAY the RESULT
    
    # Ask the USER for another INPUT
    
    # Repeat the MAIN PROGRAM until the user enter 'STOP'
    
    # END MAIN PROGRAM


if __name__ == "__main__":
    main()



</cell>
<text>
Exercise 1.10
Write a Python program to find the sum of all the positive integers below 10 that are multiples of 3 or 5.


</text>
<cell>
# START Definition of FUNCTIONS


def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 6, 9, 12, 15, 18 and 21. The sum of these multiples is 63.
    Return the sum of all the multiples of 3 or 5 below 10.
    """    
    
    sum = 0
    for n in range(3, int(math.sqrt(10)) + 1):
        if n % 3 == 0:
            sum += n
        if n % 5 == 0:
            sum += n
    return sum

# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    
    # Get the DATA entered by the USER
    
    # Analyse the DATA
    
    # Generate the RESULT
    
    # DISPLAY the RESULT
    
    # Ask the USER for another INPUT
    
    # Repeat the MAIN PROGRAM until the user enter 'STOP'
    
    # END MAIN PROGRAM


if __name__ == "__main__":
    main()



</cell>
<text>
Exercise 1.11
Write a Python program to find the sum of all the positive integers below 100 that are multiples of 3 or 5.


</text>
<cell>
# START Definition of FUNCTIONS


def multiples():
    """
    If we list all the natural numbers below 100 that are multiples of 3 or 5, we get 3, 6, 9, 12, 15, 18 and 21. The sum of these multiples is 63.
    Return the sum of all the multiples of 3 or 5 below 100.
    """    
    
    sum = 0
    for n in range(3, int(math.sqrt(100)) + 1):
        if n % 3 == 0:
            sum += n
        if n % 5 == 0:
            sum += n
    return sum

# END Definition of FUNCTIONS


