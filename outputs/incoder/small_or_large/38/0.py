
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "large" if n >= 15 (and neither if 2 <= n < 15).
    """
    if n < 2:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "small"


# Function to print a table of results
def print_table(table):
    """
        Print a table of results (as returned by print_results).
    """
    
    # Print header
    print("\nResults:")
    print("-" * 20)
    print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
    print("-" * 20)
    
    # Print results
    for row in table:
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
    print("-" * 20)


# Function to print a table of results
def print_results(table, verbose=True):
    """
        Print a table of results (as returned by print_results).
    """
    
    # Print header
    print("\nResults:")
    print("-" * 20)
    print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
    print("-" * 20)
    
    # Print results
    for row in table:
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
    print("-" * 20)
    
    # Print summary
    if verbose:
        print("\nSummary:")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15}{:<15}".format(*row) for row in table]) + " |")
        print("-" * 20)
        print("| " + " | ".join(["{:<15}{:<15}{:<15