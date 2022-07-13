
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with six underscores and True otherwise.
    """
    return re.search(r'[a-z]{6}_', text) is None

def main():
    print(joined_sequence('abcdef_ghijkl'))
    print(joined_sequence('abcdefghijkl'))

if __name__ == '__main__':
    main()