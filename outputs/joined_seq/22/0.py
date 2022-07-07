
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with a plus and False otherwise.
    """
    return re.search(r'[A-Z]+\+[A-Z]+', text) is not None

def main():
    print(joined_sequence('ABC+DEF'))
    print(joined_sequence('ABCDEF'))
    print(joined_sequence('ABC+DEF+GHI'))
    print(joined_sequence('ABC+DEF+GHI+JKL'))
    print(joined_sequence('ABC+DEF+GHI+JKL+MNO'))
    print(joined_sequence('ABC+DEF+GHI+JKL+MNO+PQRSTUVWXYZ'))

if __name__ == '__main__':
    main()