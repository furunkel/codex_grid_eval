
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of the space character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % 128
    sum += ord(' ')
    return chr(sum)


def main():
    """
    Main function
    """
    string = input("Enter a string: ")
    print("Check sum is " + checksum(string))


if __name__ == "__main__":
    main()