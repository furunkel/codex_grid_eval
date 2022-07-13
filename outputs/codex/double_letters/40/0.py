
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every letter.
    All other characters should be output a single time each.
    """
    result = ""
    for char in string:
        if char == "?":
            result += "??"
        elif char.isalpha():
            result += char * 3
        else:
            result += char
    return result


def double_letters_test():
    """
    Test for double_letters
    """
    assert double_letters("Hello") == "HHHeeellllllooo"
    assert double_letters("Hello??") == "HHHeeellllllooo???"
    assert double_letters("??") == "?????"
    assert double_letters("?Hello?") == "????HHHeeellllllooo???"
    assert double_letters("") == ""
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello??") == "????HHHeeellllllooo?????"
    assert double_letters("?Hello?