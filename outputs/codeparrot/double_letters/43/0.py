
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random string.')
    parser.add_argument('-n', '--num', type=int, default=1, help='The number of random characters to generate.')
    parser.add_argument('-s', '--string', type=str, default='Hello World!', help='The string to generate.')
    args = parser.parse_args()

    # Generate random string
    random_string = random.choice(string.ascii_lowercase)
    print(random_string)

    # Generate random string with letters
    random_string_letters = random.choice(string.ascii_lowercase)
    print(random_string_letters)

    # Generate random string with letters
    random_string_letters_letters = random.choice(string.ascii_lowercase)
    print(random_string_letters_letters)

    # Generate random string with letters and numbers
    random_string_letters_numbers = random.choice(string.ascii_lowercase)
    print(random_string_letters_numbers)

    # Generate random string with letters and numbers
    random_string_letters_letters_numbers = random.choice(string.ascii_lowercase)
    print(random_string_letters_letters_numbers)

    # Generate random string with letters and numbers
    random_string_letters_letters_numbers_letters = random.choice(string.ascii_lowercase)
    print(random_string_letters_letters_letters_numbers_letters)

    # Generate random string with letters and numbers
    random_string_letters_letters_numbers_letters_letters = random.choice(string.ascii_lowercase)
    print(random_string_letters_letters_letters_letters_letters_letters)

    # Generate random string with letters and numbers
    random_string_letters_letters_letters_letters_letters = random.choice(string.ascii_lowercase)
    print(random_string_letters_letters_letters_letters_letters_letters)

    # Generate random string with letters and numbers
    random_string_letters_letters_letters_letters_letters_