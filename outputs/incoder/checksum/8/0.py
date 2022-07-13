
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    if checksum == ord("X"):
        print("Check sum is X")
    else:
        print("Check sum is {}".format(chr(checksum)))


# Problem 4
def checksum_2(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    if checksum == ord("X"):
        print("Check sum is X")
    else:
        print("Check sum is {}".format(chr(checksum)))


# Problem 5
def checksum_3(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    if checksum == ord("X"):
        print("Check sum is X")
    else:
        print("Check sum is {}".format(chr(checksum)))


# Problem 6
def checksum_4(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 256
    if checksum == ord("X"):
        print("Check sum is X")
    else:
        print("Check sum is {}".format(chr(checksum)))


# Problem 7
def checksum_5(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum