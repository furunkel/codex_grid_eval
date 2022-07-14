def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of the space character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for c in string:
        sum = sum * 256 + ord(c)
    return sum % 64


def main():
    """
    Main function
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum of a given string')
    parser.add_argument('-i', '--input', help='The input string to check sum of')
    parser.add_argument('-o', '--output', help='The output string to check sum of')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
    args = parser.parse_args()

    # Check sum of
    if args.input == None or args.output == None:
        print "Error: No input string specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output == None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: Both input and output must be specified"
        sys.exit(1)

    # Check sum of
    if args.input != None and args.output != None:
        print "Error: