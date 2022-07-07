
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with an underscore and True otherwise.
    """
    return re.search(r'[a-z]+_[a-z]+', text) is None

def main():
    print(joined_sequence('abc_def'))
    print(joined_sequence('abcdef'))

if __name__ == '__main__':
    main()