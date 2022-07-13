
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10 and 12. The product of these multiples is 97200.
    Return the product of all the multiples of 3 or 5 below 197.
    """    
    
    multiples = []
    
    for n in range(2, int(math.sqrt(197)) + 1):
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
            
    return sum(multiples)

# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    
    # Get the number of test cases
    number_of_test_cases = int(input("Number of test cases: "))
    
    # Empty List to contain the RESULTS of each test case (integer values)
    number_of_results = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    averages = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    maximums = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    minimums = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    sums = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    products = []
    
    # Empty List to contain the RESULTS of each test case (integer values)
    
    # Acquisition and Control of the DATA entered by the USER
    
    # Get the number of test cases
    for n in range(1, number_of_test_cases + 1):
        
        # Get the number of the test case
        test_case_number = n
        
        # Get the number of test case results
        number_of_results.append(int(input("Number of results for test case " + str(test_case_number) + ": ")))
        
        # Get the average of the test case results
        averages.append(float(sum(number_of_results[test_case_number - 1])/ number_of_results[test_case_number - 1]))
        
        # Get the maximum of the test case results
        maximums.append(max(number_of_results[test_case_number - 1]))
        
        # Get the minimum of the test case results
        minimums.append(min(number_of_results[test_case_number - 1]))
        
        # Get the sum of the test case results
        sums.append(sum(number_of_results[test_case_number - 1]))
        
        # Get the product of the test case results
        products.append(multiples())
        
    # Displaying the RESULTS
    
    # Displaying the RESULTS of each test case (integer values)
    print("Results:")
    print("-" * 60)
    
    # Displaying the RESULTS of each test case (integer values)
    print("Test Case #" + str(test_case_number) + ":")
    print("-" * 60)
    
    # Displaying the RESULTS of each test case (integer values)
    print("Average of " + str(number_of_results[test_case_number - 1]) + " results: " + str(averages[test_case_number - 1]))
    print("Maximum of 