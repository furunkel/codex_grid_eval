
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of an exclamation mark, and then convert that integer back
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
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    args = parser.parse_args()

    # Check arguments
    if args.verbose:
        print("Checking sum on file: " + args.file)

    # Open file
    with open(args.file, 'r') as f:
        sum = sum_on_file(f)

    # Print results
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(sum)))
    print("Checksum: " + str(checksum(