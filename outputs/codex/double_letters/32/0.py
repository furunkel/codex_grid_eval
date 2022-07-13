
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every letter.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char == "!":
            new_string += "!!"
        elif char.isalpha():
            new_string += char * 3
        else:
            new_string += char
    return new_string


def double_letters_test():
    assert double_letters("Hello!") == "HHHeeellllllooo!!!"
    assert double_letters("Hello") == "HHHeeellllllooo"
    assert double_letters("Hello World!") == "HHHeeellllllooo   WWWooorrllddd!!!"
    assert double_letters("Hello World") == "HHHeeellllllooo   WWWooorrllddd"
    assert double_letters("") == ""
    assert double_letters("!") == "!!"
    assert double_letters("a") == "aaa"
    assert double_letters("a!") == "aaa!!"
    assert double_letters("!a") == "!!a"
    assert double_letters("!a!") == "!!a!!"
    assert double_letters("!a!a") == "!!a!!aaa"
    assert double_letters("!a!a!") == "!!a!!aaa!!"
    assert double_letters("!a!a!a") == "!!a!!aaa!!aaa"
    assert double_letters("!a!a!a!") == "!!a!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a") == "!!a!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!a!") == "!!a!!aaa!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a!a") == "!!a!!aaa!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!a!a!") == "!!a!!aaa!!aaa!!aaa!!aaa!!"
    assert double_letters("!a!a!a!a!a!a") == "!!a!!aaa!!aaa!!aaa!!aaa!!aaa"
    assert double_letters("!a!a!a!a!a!a!")