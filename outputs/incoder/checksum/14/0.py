
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    checksum += ord("!")
    checksum = checksum % 256
    return chr(checksum)


def checksum_test(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_2(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char2:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_3(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char3:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_4(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char4:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_5(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char5:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_6(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char6:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_7(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char7:
        print("Check sum is correct.")
    else:
        print("Check sum is incorrect.")


def checksum_test_8(string):
    """
    Use this function to test the checksum function by passing a string into the function.
    """
    checksum = checksum(string)
    if checksum == checksum_char8: