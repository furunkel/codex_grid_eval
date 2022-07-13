
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Create a list of all the words in the file.
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels = []
    with open('vowels.txt', 'r') as f:
        for line in f:
            vowels.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_lower = []
    with open('vowels_lower.txt', 'r') as f:
        for line in f:
            vowels_lower.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_upper = []
    with open('vowels_upper.txt', 'r') as f:
        for line in f:
            vowels_upper.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_lower_lower = []
    with open('vowels_lower_lower.txt', 'r') as f:
        for line in f:
            vowels_lower_lower.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_upper_lower = []
    with open('vowels_upper_lower.txt', 'r') as f:
        for line in f:
            vowels_upper_lower.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_lower_upper = []
    with open('vowels_lower_upper.txt', 'r') as f:
        for line in f:
            vowels_lower_upper.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_upper_lower_lower = []
    with open('vowel