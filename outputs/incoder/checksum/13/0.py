
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for character in string:
        sum += ord(character)
    checksum = sum % 128
    if checksum == 128:
        checksum = '!'
    elif checksum == 0:
        checksum = '.'
    else:
        checksum = chr(checksum)
    return checksum


# Checksum
def checksum_2(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for character in string:
        sum += ord(character)
    checksum = sum % 128
    if checksum == 128:
        checksum = '!'
    elif checksum == 0:
        checksum = '.'
    else:
        checksum = chr(checksum)
    return checksum


# Checksum
def checksum_3(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for character in string:
        sum += ord(character)
    checksum = sum % 128
    if checksum == 128:
        checksum = '!'
    elif checksum == 0:
        checksum = '.'
    else:
        checksum = chr(checksum)
    return checksum


# Checksum
def checksum_4(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for character in string:
        sum += ord(character)
    checksum = sum % 128
    if checksum == 128:
        checksum = '!'
    elif checksum == 0:
        checksum = '.'
    else:
        checksum = chr(checksum)
    return checksum


# Checksum
def checksum_5(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of an exclamation mark, and then 