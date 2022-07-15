def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, sqrt(i)) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    5
    Then, the output should be:
    {1: 1.0, 2: 1.414, 3: 1.732, 4: 2.0, 5: 2.236}

    """
    # Initialize the dictionary
    dict = {}
    # Loop through the integral number n
    for i in range(1, n + 1):
        # If i is a power of 2, then the power of 2 is the power of 2^n
        if i % 2 == 0:
            # If i is a power of 2^n, then the power of 2^n is the power of 2^n^2
            if i % 2 == 1:
                # If i is a power of 2^n^2, then the power of 2^n^2 is the power of 2^n^2^2
                if i % 2 == 2:
                    # If i is a power of 2^n^2^2, then the power of 2^n^2^2 is the power of 2^n^2^2^2^2
                    if i % 2 == 3:
                        # If i is a power of 2^n^2^2^2, then the power of 2^n^2^2^2^2 is the power of 2^n^2^2^2^2^2^2^2
                        if i % 2 == 4:
                            # If i is a power of 2^n^2^2^2^2, then the power of 2^n^2^2^2^2^2 is the power of 2^n^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^2^