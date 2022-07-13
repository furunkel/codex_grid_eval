
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of uppercase letters joined with two underscores and False otherwise.
    """
    return bool(re.search(r'[A-Z]{2}__[A-Z]{2}', text))

def main():
    print(joined_sequence('AA__BB'))
    print(joined_sequence('A__B'))
    print(joined_sequence('A__B_'))
    print(joined_sequence('A__BB'))
    print(joined_sequence('A__BB_'))
    print(joined_sequence('A__BBB'))
    print(joined_sequence('A__BBB_'))
    print(joined_sequence('A__BBBB'))
    print(joined_sequence('A__BBBB_'))
    print(joined_sequence('A__BBBBB'))
    print(joined_sequence('A__BBBBB_'))
    print(joined_sequence('A__BBBBBB'))
    print(joined_sequence('A__BBBBBB_'))
    print(joined_sequence('A__BBBBBBB'))
    print(joined_sequence('A__BBBBBBB_'))
    print(joined_sequence('A__BBBBBBBB'))
    print(joined_sequence('A__BBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBBBBBB_'))
    print(joined_sequence('A__BBBBBBBBBBBBBB'))
    print(joined_sequence('A__BBBBBBBBBBBBBB_'))
