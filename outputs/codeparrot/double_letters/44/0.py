def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random string.')
    parser.add_argument('-n', '--name', help='The name of the random string.')
    parser.add_argument('-s', '--seed', help='The seed for the random string.')
    parser.add_argument('-l', '--length', help='The length of the random string.')
    parser.add_argument('-e', '--exponent', help='The exponent of the random string.')
    parser.add_argument('-d', '--decimal', help='The decimal number of the random string.')
    parser.add_argument('-r', '--random', help='The random string.')
    parser.add_argument('-s2', '--s2', help='The string to be used for the random string.')
    parser.add_argument('-e2', '--e2', help='The string to be used for the random string.')
    parser.add_argument('-d2', '--d2', help='The string to be used for the random string.')
    parser.add_argument('-r2', '--r2', help='The string to be used for the random string.')
    parser.add_argument('-e3', '--e3', help='The string to be used for the random string.')
    parser.add_argument('-d3', '--d3', help='The string to be used for the random string.')
    parser.add_argument('-r3', '--r3', help='The string to be used for the random string.')
    parser.add_argument('-e4', '--e4', help='The string to be used for the random string.')
    parser.add_argument('-d4', '--d4', help='The string to be used for the random string.')
    parser.add_argument('-r4', '--r4', help='The string to be used for the random string.')
    parser.add_argument('-e5', '--e5', help='The string to be used for the random string.')