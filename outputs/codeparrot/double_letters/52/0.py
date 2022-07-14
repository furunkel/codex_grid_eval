def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate a random string.')
    parser.add_argument('-n', '--name', help='Name of the random string.')
    parser.add_argument('-l', '--length', help='Length of the random string.')
    parser.add_argument('-s', '--seed', help='Seed for the random string.')
    parser.add_argument('-e', '--encoding', help='Encoding of the random string.')
    parser.add_argument('-d', '--debug', help='Debug mode.')
    parser.add_argument('-o', '--output', help='Output file.')
    parser.add_argument('-p', '--print', help='Print the generated random string.')
    parser.add_argument('-r', '--random', help='Generate a random string.')
    parser.add_argument('-s2', '--random2', help='Generate a random string.')
    parser.add_argument('-t', '--test', help='Test the generated random string.')
    parser.add_argument('-v', '--verbose', help='Verbose mode.')
    args = parser.parse_args()

    # Check arguments
    if args.name is None:
        parser.print_help()
        sys.exit(1)

    # Check seed
    if args.seed is None:
        args.seed = random.randint(0, sys.maxint)

    # Check encoding
    if args.encoding is None:
        args.encoding = 'utf-8'

    # Check output file
    if args.output is None:
        args.output = args.random

    # Check print
    if args.print is None:
        args.print = args.random

    # Check print2
    if args.print2 is None:
        args.print2 = args.random2

    # Check test
    if args.test is None:
        args.test = args.random

    # Check length
    if args.length is None:
        args.length = random.randint(1, sys.