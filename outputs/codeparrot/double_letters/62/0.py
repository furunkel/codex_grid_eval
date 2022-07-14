def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return "".join([c for c in string if c.isalpha()])


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="A simple tool to generate a wordlist from a file.")
    parser.add_argument("-i", "--input", help="The file to read from.")
    parser.add_argument("-o", "--output", help="The file to write to.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")
    args = parser.parse_args()

    # Read input file
    with open(args.input, "r") as f:
        lines = f.readlines()

    # Read each line
    for line in lines:
        # Split line into words
        words = line.split()

        # Create a list of words
        words = [w.lower() for w in words]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if w not in stopwords]

        # Create a list of words
        words = [w for w in words if