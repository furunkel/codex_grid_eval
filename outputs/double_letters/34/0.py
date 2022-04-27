
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "!":
            new_string += char * 2
        elif char.isupper():
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_test():
    assert double_letters("Hello!") == "HHelloo!!"
    assert double_letters("Hello World!") == "HHHeeelllloo WWoorrlldd!!"
    assert double_letters("Hello World! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello! Hello! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!! HHelloo!!"
    assert double_letters("Hello World! Hello! Hello! Hello! Hello! Hello! Hello! Hello! Hello!") == "HHHeeelllloo WWoorrlldd!! HHelloo!! HHelloo!! HHelloo!!