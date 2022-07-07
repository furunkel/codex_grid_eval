
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a minus and True otherwise.
    """
    return re.search(r'[a-z]+-[a-z]+', text) is None

def main():
    print(joined_sequence('abc-def'))
    print(joined_sequence('abcdef'))

if __name__ == '__main__':
    main()