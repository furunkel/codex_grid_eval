def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random password.')
    parser.add_argument('-n', '--name', help='The name of the password.', required=True)
    parser.add_argument('-p', '--password', help='The password to generate.', required=True)
    parser.add_argument('-c', '--letters', help='The letters to generate.', required=True)
    parser.add_argument('-r', '--random', help='Generate a random password.', action='store_true')
    parser.add_argument('-s', '--salt', help='Generate a random password.', action='store_true')
    parser.add_argument('-t', '--test', help='Test the password.', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose output.', action='store_true')
    args = parser.parse_args()

    # Check if the password is valid
    if args.password is None:
        print('Password must be specified.')
        sys.exit(1)

    # Check if the letters are valid
    if args.letters is None:
        print('Letters must be specified.')
        sys.exit(1)

    # Check if the random password is valid
    if args.random is None:
        print('Random password must be specified.')
        sys.exit(1)

    # Check if the test password is valid
    if args.test is None:
        print('Test password must be specified.')
        sys.exit(1)

    # Check if the verbose flag is set
    if args.verbose:
        print('Verbose output enabled.')

    # Create the password generator
    password_generator = PasswordGenerator()

    # Generate a random password
    password = password_generator.generate_password()

    # Print the password
    print(password)

    # Print the letters
    print(double_letters(password))

    # Print the random password
    print(double_letters(password))

    # Print the test password
    print(