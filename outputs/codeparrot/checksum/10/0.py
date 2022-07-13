
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of lowercase u, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum on a file.')
    parser.add_argument('-f', '--file', help='File to check sum on.')
    parser.add_argument('-d', '--directory', help='Directory to check sum on.')
    parser.add_argument('-c', '--checksum', help='Checksum of the file.')
    args = parser.parse_args()

    # Check sum
    if args.file is None:
        print "Error: No file specified."
        sys.exit(1)

    # Check sum
    if args.directory is None:
        print "Error: No directory specified."
        sys.exit(1)

    # Check sum
    if args.checksum is None:
        print "Error: No checksum specified."
        sys.exit(1)

    # Check sum
    if args.checksum == None:
        print "Error: No checksum specified."
        sys.exit(1)

    # Check sum
    if args.checksum != None:
        if args.checksum == "X":
            print "Error: Checksum is X"
        else:
            print "Error: Checksum is not X"
            sys.exit(1)

    # Check sum
    if args.checksum == None:
        print "Error: No checksum specified."
        sys.exit(1)

    # Check sum
    if args.checksum != None:
        if args.checksum == "X":
            print "Error: Checksum is X"
        else:
            print "Error: Checksum is not X"
            sys.exit(1)

    # Check sum
    if args.checksum != None:
        if args.checksum == "X":
            print "Error: Checksum is X"
        else:
            print "Error: Checksum is not X"
            sys.exit(1)

    # Check sum
    if args.checksum != None:
        if args.checksum == "X":
            print "Error: Checksum is X"
       