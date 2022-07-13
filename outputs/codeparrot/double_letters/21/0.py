
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple python script to generate a random string.')
    parser.add_argument('-n', '--name', help='The name of the random string.', required=True)
    parser.add_argument('-s', '--seed', help='The seed for the random string.', required=True)
    parser.add_argument('-l', '--length', help='The length of the random string.', required=True)
    parser.add_argument('-e', '--encoding', help='The encoding of the random string.', required=True)
    parser.add_argument('-d', '--debug', help='Enable debug output.', action='store_true')
    parser.add_argument('-t', '--test', help='Test the random string.', action='store_true')
    parser.add_argument('-v', '--verbose', help='Enable verbose output.', action='store_true')
    args = parser.parse_args()

    # Set seed
    random.seed(args.seed)

    # Set the name
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the length
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the encoding
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the test
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the verbose
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the length
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace(' ', '_')

    # Set the encoding
    random_string = random.choice(string.ascii_lowercase)
    random_string = random_string.replace('