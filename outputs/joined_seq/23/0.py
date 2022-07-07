
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a plus and False otherwise.
    """
    return re.search(r'[a-z]+\+[a-z]+', text)

def main():
    print(joined_sequence('abc+def'))
    print(joined_sequence('abcdef'))

if __name__ == '__main__':
    main()