
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random string.')
    parser.add_argument('-n', '--name', help='The name of the random string.', required=True)
    parser.add_argument('-s', '--string', help='The string to be generated.', required=True)
    parser.add_argument('-l', '--length', help='The length of the string.', required=True)
    parser.add_argument('-e', '--encoding', help='The encoding of the string.', required=True)
    parser.add_argument('-d', '--delimiter', help='The delimiter of the string.', required=True)
    parser.add_argument('-t', '--type', help='The type of the string.', required=True)
    parser.add_argument('-r', '--random', help='The random string.', required=True)
    parser.add_argument('-l', '--length-random', help='The length of the random string.', required=True)
    parser.add_argument('-e', '--encoding-random', help='The encoding of the random string.', required=True)
    parser.add_argument('-d', '--delimiter-random', help='The delimiter of the random string.', required=True)
    parser.add_argument('-t', '--type-random', help='The type of the random string.', required=True)
    parser.add_argument('-r', '--random-random', help='The random string.', required=True)
    parser.add_argument('-l', '--length-random-random', help='The length of the random string.', required=True)
    parser.add_argument('-e', '--encoding-random-random', help='The encoding of the random string.', required=True)
    parser.add_argument('-d', '--delimiter-random-random-random', help='The delimiter of the random string.', required=True)
    parser.add_argument('-t', '--type-random-random-random-random', help='The type of the random string.', required=True)
    parser