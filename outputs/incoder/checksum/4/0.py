
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of the newline character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 128
    checksum += 128
    checksum = chr(checksum)
    return checksum

def checksum_test(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_2(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_3(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_4(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_5(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_6(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + checksum)
    print("Expected checksum is " + checksum_expected)
    print("Correct checksum is " + str(correct))
    return correct

def checksum_test_7(string):
    """
    Checks the checksum function by comparing its output to the expected output.
    """
    checksum = checksum(string)
    correct = checksum == checksum_expected
    print("Checksum is " + 