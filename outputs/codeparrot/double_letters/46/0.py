def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    # The main function.
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
    # Create a list of all the letters in the file.
    letters = []
    with open('letters.txt', 'r') as f:
        for line in f:
            letters.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_and_letters = []
    with open('vowels_and_letters.txt', 'r') as f:
        for line in f:
            vowels_and_letters.append(line.strip())
    # Create a list of all the letters in the file.
    letters_and_vowels = []
    with open('letters_and_vowels.txt', 'r') as f:
        for line in f:
            letters_and_vowels.append(line.strip())
    # Create a list of all the vowels in the file.
    vowels_and_letters_and_vowels = []
    with open('vowels_and_letters_and_vowels.txt', 'r') as f:
        for line in f:
            vowels_and_letters_and_vowels.append(line.strip())
    # Create a list of all the letters in the file.
    letters_and_letters_and_letters_and_vowels_and_letters = []
    with open('letters_and_letters_and_letters_and_vowels_and_letters_and_letters_and_vowels_and_letters_and_vowels_and_letters_