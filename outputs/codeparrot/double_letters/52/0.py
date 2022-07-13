
def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple program to generate a random string.')
    parser.add_argument('-n', '--name', help='The name of the random string.', required=True)
    parser.add_argument('-p', '--password', help='The password of the random string.', required=True)
    parser.add_argument('-l', '--letters', help='The letters to generate.', required=True)
    parser.add_argument('-e', '--exclamation', help='The exclamation point to generate.', required=True)
    args = parser.parse_args()

    # Create a random string
    random_string = random.choice(string.ascii_lowercase)

    # Create a random string from the list of letters
    random_string_list = []
    for letter in string.ascii_lowercase:
        random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of exclamation points
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of exclamation points
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of letters
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of exclamation points
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of letters
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of exclamation points
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of letters
    random_string_list.append(random.choice(string.ascii_lowercase))

    # Create a random string from the list of exclamation points
   