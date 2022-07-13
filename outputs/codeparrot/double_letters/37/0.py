
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every question mark.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Get the command line arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "input=", "output="])
    except getopt.GetoptError:
        print "Usage: python double_letters.py -i <input> -o <output>"
        sys.exit(2)
    # Get the input file.
    try:
        input_file = open(args[0], "r")
    except IOError:
        print "Error: File not found: " + args[0]
        sys.exit(2)
    # Get the output file.
    try:
        output_file = open(args[1], "w")
    except IOError:
        print "Error: File not found: " + args[1]
        sys.exit(2)
    # Get the number of questions.
    try:
        num_questions = int(args[2])
    except ValueError:
        print "Error: Number of questions must be an integer."
        sys.exit(2)
    # Get the number of questions per question.
    try:
        num_questions_per_question = int(args[3])
    except ValueError:
        print "Error: Number of questions per question must be an integer."
        sys.exit(2)
    # Get the number of questions per question.
    try:
        num_questions_per_question = int(args[4])
    except ValueError:
        print "Error: Number of questions per question must be an integer."
        sys.exit(2)
    # Get the number of questions per question.
    try:
        num_questions_per_question = int(args[5])
    except ValueError:
        print "Error: Number of questions per question must be an integer."
        sys.exit(2)
    # Get the number of questions per question.
    try:
        num_questions_per_question = int(args[6])
    except ValueError:
        print "Error: Number of questions per question must be an integer."
        sys.exit(2)
    # Get the number of questions per question.
    try: