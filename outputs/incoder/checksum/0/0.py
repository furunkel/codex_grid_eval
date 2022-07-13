
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of the space character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for character in string:
        checksum += ord(character)
    checksum = checksum % 64
    checksum += 32
    checksum = chr(checksum)
    return checksum


def checksum_valid(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid2(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid3(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid4(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid5(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid6(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid7(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid8(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid9(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid10(checksum):
    """
    Given a checksum character, determine if the checksum character is valid or not.
    """
    checksum = ord(checksum)
    if checksum == 32:
        return True
    else:
        return False


def checksum_valid11(checksum):
    """
    Given a checksum character, determine if the checksum