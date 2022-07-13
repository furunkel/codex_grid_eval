
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "!":
            new_string += "!!"
        elif char.islower():
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_test():
    assert double_letters("Hello!") == "HHHeeelllloo!!"
    assert double_letters("Hello") == "HHHeeellllooo"
    assert double_letters("Hello World!") == "HHHeeelllloo   WWWooorrlldd!!"
    assert double_letters("Hello World") == "HHHeeelllloo   WWWooorrlldd"
    assert double_letters("") == ""
    assert double_letters("a") == "aaa"
    assert double_letters("A") == "A"
    assert double_letters("!") == "!!"
    assert double_letters("!!!") == "!!!!!"
    assert double_letters("!a") == "!!aaa"
    assert double_letters("a!") == "aaa!!"
    assert double_letters("a!a") == "aaa!!aaa"
    assert double_letters("!a!a") == "!!aaa!!aaa"
    assert double_letters("!a!a!") == "!!aaa!!aaa!!"
    assert double_letters("!a!a!a") == "!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!") == "!!aaa!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a") == "!!aaa!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!a!") == "!!aaa!!aaa!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a!a") == "!!aaa!!aaa!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!a!a!") == "!!aaa!!aaa!!aaa!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a!a!a") == "!!aaa!!aaa!!aaa!!aaa!!aaa!!aaa"
