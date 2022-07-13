
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of an exclamation mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    checksum = 0
    for char in string:
        checksum += ord(char)
    checksum = checksum % 64
    checksum += 63
    checksum = chr(checksum)
    return checksum


# Checksum for "A"
checksum(letters[0])

# Checksum for "B"
checksum(letters[1])

# Checksum for "C"
checksum(letters[2])

# Checksum for "D"
checksum(letters[3])

# Checksum for "E"
checksum(letters[4])

# Checksum for "F"
checksum(letters[5])

# Checksum for "G"
checksum(letters[6])

# Checksum for "H"
checksum(letters[7])

# Checksum for "I"
checksum(letters[8])

# Checksum for "J"
checksum(letters[9])

# Checksum for "K"
checksum(letters[10])

# Checksum for "L"
checksum(letters[11])

# Checksum for "M"
checksum(letters[12])

# Checksum for "N"
checksum(letters[13])

# Checksum for "O"
checksum(letters[14])

# Checksum for "P"
checksum(letters[15])

# Checksum for "Q"
checksum(letters[16])

# Checksum for "R"
checksum(letters[17])

# Checksum for "S"
checksum(letters[18])

# Checksum for "T"
checksum(letters[19])

# Checksum for "U"
checksum(letters[20])

# Checksum for "V"
checksum(letters[21])

# Checksum for "W"
checksum(letters[22])

# Checksum for "X"
checksum(letters[23])

# Checksum for "Y"
checksum(letters[24])

# Checksum for "Z"
checksum(letters[25])

# Checksum for "!"
checksum(letters[26])

# Checksum for "?"
checksum(letters[27])

# Checksum for "@"
checksum(letters[28])

# Checksum for "A"
checksum(letters[29])

# Checksum for "B"
checksum(letters[30])

# Checksum for "C"
checksum(letters[31])

# Checksum for "D"
checksum(letters[