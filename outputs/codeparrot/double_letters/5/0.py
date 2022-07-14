def double_letters(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random string.')
    parser.add_argument('-n', '--num', type=int, default=1, help='The number of random characters to generate.')
    parser.add_argument('-s', '--seed', type=int, default=1, help='The seed for the random number generator.')
    parser.add_argument('-l', '--length', type=int, default=10, help='The length of the generated string.')
    parser.add_argument('-c', '--chars', type=str, default='abcdefghijklmnopqrstuvwxyz', help='The characters to generate.')
    parser.add_argument('-p', '--question', type=str, default='What is the question?', help='The question to generate.')
    parser.add_argument('-r', '--random', action='store_true', help='Randomly generate a random string.')
    parser.add_argument('-s2', '--shuffle', action='store_true', help='Shuffle the string.')
    parser.add_argument('-r2', '--random2', action='store_true', help='Randomly generate a random string.')
    parser.add_argument('-s3', '--shuffle3', action='store_true', help='Shuffle the string.')
    parser.add_argument('-r3', '--random3', action='store_true', help='Randomly generate a random string.')
    parser.add_argument('-s4', '--shuffle4', action='store_true', help='Shuffle the string.')
    parser.add_argument('-r4', '--random4', action='store_true', help='Randomly generate a random string.')
    parser.add_argument('-s5', '--shuffle5', action='store_true', help='Shuffle the string.')
    parser.add_argument('-r5', '--random5', action='store_true', help='Randomly generate a random string.')
    parser.add_argument('-s6', '--shuffle6', action='store_true', help