
def checksum(str):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for c in str:
        sum += ord(c)
    sum = sum % 64
    sum += ord('X')
    return chr(sum)

def main():
    """
    Main function
    """
    print("Check sum is " + checksum(input("Enter a string: ")))

if __name__ == "__main__":
    main()