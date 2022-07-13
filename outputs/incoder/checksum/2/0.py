
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of the space character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    checksum += 32
    checksum = chr(checksum)
    return checksum

def checksum_test(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_2(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_3(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_4(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_5(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_6(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_7(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_8(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_9(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_10(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_11(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_12(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)

def checksum_test_13(string):
    """
    Print the checksum character for given string.
    """
    checksum = checksum(string)
    print("Check sum is %s" % checksum)