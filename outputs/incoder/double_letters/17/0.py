
def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every number.
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter.isupper():
            double_letters += letter * 2
        elif letter.isdigit():
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters

# Test Cases
assert double_letters("Hello") == "HHHeeellllllo"
assert double_letters("How are you?") == "HOW ARE YOU?"
assert double_letters("9876543210") == "98765432100"
assert double_letters("aA") == "aaa"
assert double_letters("abB") == "aabb"
assert double_letters("abBcC") == "aabbcc"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCdD") == "aabbccdD"
assert double_letters("abBcCd