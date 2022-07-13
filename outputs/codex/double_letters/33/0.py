
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every number.
    All other characters should be output a single time each.
    """
    new_string = ""
    for char in string:
        if char.isdigit():
            new_string += char * 3
        elif char == "!":
            new_string += char * 2
        else:
            new_string += char
    return new_string


def double_letters_test():
    assert double_letters("Hello!") == "Hello!!"
    assert double_letters("Hello!!!") == "Hello!!!!"
    assert double_letters("Hello1") == "Hello111"
    assert double_letters("Hello1!") == "Hello111!!"
    assert double_letters("Hello1!!!") == "Hello111!!!!"
    assert double_letters("Hello1!!!!") == "Hello111!!!!!"
    assert double_letters("Hello1!!!!!") == "Hello111!!!!!!"
    assert double_letters("Hello1!!!!!!") == "Hello111!!!!!!!!"
    assert double_letters("Hello1!!!!!!!") == "Hello111!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!") == "Hello111!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!!!!!!"
    assert double_letters("Hello1!!!!!!!!!!!!!!!!!!!!!!!!!") == "Hello111!!!!!!!!!!!!!!!!!!!!!!!!!!"
    assert double_letters