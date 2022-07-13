
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters = ""
    for letter in string:
        if letter in "aeiouAEIOU":
            double_letters += letter * 2
        elif letter in "AEIOUaeiou":
            double_letters += letter * 3
        else:
            double_letters += letter
    return double_letters

# TESTS
assert double_letters("hello") == "hheelllloo"
assert double_letters("hello ") == "hheelllloo"
assert double_letters("hElLo") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letters("hElL") == "hheelllloo"
assert double_letter