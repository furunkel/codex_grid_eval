
def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a plus and True otherwise.
    """
    return re.search(r'[A-Z]+\+[A-Z]+', text) is None

def main():
    print(joined_sequence('ABC+DEF'))
    print(joined_sequence('ABCDEF'))
    print(joined_sequence('ABC+D+EF'))

if __name__ == '__main__':
    main()