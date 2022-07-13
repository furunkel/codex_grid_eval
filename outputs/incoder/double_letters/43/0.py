
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    doubled_string = ""
    for letter in string:
        if letter == "?":
            doubled_string += "?" + letter
        elif letter.islower():
            doubled_string += letter + "?"
        else:
            doubled_string += letter
    return doubled_string


@given('the string "{string}" is {expected} the string "{expected_doubled}"')
def double_letters_test(string, expected, expected_doubled):
    assert double_letters(string) == expected_doubled


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_2(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_3(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_4(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_5(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_6(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')
def double_letters_test_7(string, expected, expected_doubled, expected_letters):
    assert double_letters(string) == expected_doubled
    assert double_letters(string) == expected_letters


@given('the string "{string}" is {expected} the string "{expected_doubled}" with {expected} and {expected} letters')