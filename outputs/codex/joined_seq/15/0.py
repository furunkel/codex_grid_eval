
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with an underscore and False otherwise.
    """
    return bool(re.search(r'[a-z]+_[a-z]+', text))

def main():
    print(joined_sequence('abc_123'))
    print(joined_sequence('abc_ABC'))
    print(joined_sequence('abcABC123'))
    print(joined_sequence('_abc_123'))
    print(joined_sequence('______'))
    print(joined_sequence('123_abc'))
    print(joined_sequence('abc_123_abc'))
    print(joined_sequence('abc_ABC_123'))
    print(joined_sequence('_abc_ABC_123'))
    print(joined_sequence('_abc_ABC_123_'))
    print(joined_sequence('_abc_ABC_123_abc'))
    print(joined_sequence('_abc_ABC_123_abc_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC_123'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC_123_'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC_123_abc'))
    print(joined_sequence('_abc_ABC_123_abc_ABC_123_abc_ABC_123_abc_'