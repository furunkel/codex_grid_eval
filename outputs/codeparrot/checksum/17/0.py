def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of a question mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for char in string:
        sum = sum + ord(char) - ord('0')
    return sum % 256


def main():
    """
    Main function.
    """
    # Create a list of all the words in the file.
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

    # Create a list of all the words in the file.
    words_set = set(words)

    # Create a list of all the words in the file.
    words_list = []
    with open('words_list.txt', 'r') as f:
        for line in f:
            words_list.append(line.strip())

    # Create a list of all the words in the file.
    words_list_set = set(words_list)

    # Create a list of all the words in the file.
    words_list_list = []
    with open('words_list_list.txt', 'r') as f:
        for line in f:
            words_list_list.append(line.strip())

    # Create a list of all the words in the file.
    words_list_list_set = set(words_list_list)

    # Create a list of all the words in the file.
    words_list_list_list = []
    with open('words_list_list_list.txt', 'r') as f:
        for line in f:
            words_list_list_list.append(line.strip())

    # Create a list of all the words in the file.
    words_list_list_list = []
    with open('words_list_list_list.txt', 'r') as f:
        for line in f:
            words_list_list_list.append(line.strip())

    # Create a list of all the words in the file.
    words_list_list_list = []
    with open