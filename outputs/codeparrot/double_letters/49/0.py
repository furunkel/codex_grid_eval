def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every number.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate a random string.')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of characters to generate.')
    parser.add_argument('-s', '--string', type=str, default='A', help='String to generate.')
    parser.add_argument('-r', '--random', action='store_true', help='Generate a random string.')
    args = parser.parse_args()

    # Generate random string
    random_string = random.choice(string.ascii_lowercase)

    # Generate random string
    random_string = random_string.upper()

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.replace(' ', '')

    # Generate random string
    random_string = random_string.