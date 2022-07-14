def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of the newline character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for c in string:
        sum = sum + ord(c) - ord('0')
    return sum % 64


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug output.')
    parser.add_argument('-s', '--silent', action='store_true', help='Silent output.')
    parser.add_argument('-p', '--print', action='store_true', help='Print output.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()

    # Check arguments
    if args.version:
        print(__version__)
        sys.exit(0)

    # Check arguments
    if args.verbose:
        print('Verbose output.')
        sys.exit(0)

    # Check arguments
    if args.silent:
        print('Silent output.')
        sys.exit(0)

    # Check arguments
    if args.print:
        print('Print output.')
        sys.exit(0)

    # Check arguments
    if args.version:
        print(__version__)
        sys.exit(0)

    # Check arguments
    if args.silent:
        print('Silent output.')
        sys.exit(0)

    # Check arguments
    if args.print:
        print('Print output.')
        sys.exit(0)

    # Check arguments
    if args.version:
        print(__version__)
        sys.exit(0)

    # Check arguments
    if args.silent:
        print('Silent output.')
        sys.exit(0)

    # Check arguments
    if args.print:
        print('Print output.')
        sys.exit(0)

    # Check arguments
    if args.version