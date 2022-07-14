def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return "".join([char for char in string if char.isupper()])


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A simple script to generate a random password.')
    parser.add_argument('-n', '--name', help='The name of the account to generate.')
    parser.add_argument('-p', '--password', help='The password to generate.')
    parser.add_argument('-c', '--character', help='The character to generate.')
    parser.add_argument('-d', '--description', help='The description of the account to generate.')
    parser.add_argument('-e', '--email', help='The email address to generate.')
    parser.add_argument('-p1', '--password1', help='The password to generate.')
    parser.add_argument('-p2', '--password2', help='The password to generate.')
    parser.add_argument('-p3', '--password3', help='The password to generate.')
    parser.add_argument('-p4', '--password4', help='The password to generate.')
    parser.add_argument('-p5', '--password5', help='The password to generate.')
    parser.add_argument('-p6', '--password6', help='The password to generate.')
    parser.add_argument('-p7', '--password7', help='The password to generate.')
    parser.add_argument('-p8', '--password8', help='The password to generate.')
    parser.add_argument('-p9', '--password9', help='The password to generate.')
    parser.add_argument('-p10', '--password10', help='The password to generate.')
    parser.add_argument('-p11', '--password11', help='The password to generate.')
    parser.add_argument('-p12', '--password12', help='The password to generate.')
    parser.add_argument('-p13', '--password13', help='The password to generate.')
    parser.add_argument('-p14', '--password14', help='The password to generate.')
    parser.add_argument('-p15', '--password15',