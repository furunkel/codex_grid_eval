
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Get the command line arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print "Error: Invalid options."
        sys.exit(2)
    # Get the input file.
    try:
        input_file = args[0]
    except IndexError:
        print "Error: No input file specified."
        sys.exit(2)
    # Get the output file.
    try:
        output_file = args[1]
    except IndexError:
        print "Error: No output file specified."
        sys.exit(2)
    # Get the number of letters.
    try:
        n = int(args[2])
    except IndexError:
        print "Error: No number of letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = args[3]
    except IndexError:
        print "Error: No lowercased letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = lowercased_letters.lower()
    except AttributeError:
        print "Error: No lowercased letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = lowercased_letters.upper()
    except AttributeError:
        print "Error: No lowercased letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = lowercased_letters.capitalize()
    except AttributeError:
        print "Error: No lowercased letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = lowercased_letters.title()
    except AttributeError:
        print "Error: No lowercased letters specified."
        sys.exit(2)
    # Get the lowercased letters.
    try:
        lowercased_letters = lowercased_letters.replace(" ", "")
    except AttributeError:
        print "Error: No lowercased