
def double_letters(string):
    """
    Given a string, return the string, doubling every letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for letter in string:
        if letter == '!':
            double_letters_string += '!!'
        elif letter == '?':
            double_letters_string += '??'
        else:
            double_letters_string += letter*2
    return double_letters_string

# Test Cases
print(double_letters('hello'))
print(double_letters('hello!'))
print(double_letters('hello?'))
print(double_letters('hello!?'))
print(double_letters('hello!?!'))
print(double_letters('hello!?!?'))
print(double_letters('hello!?!?!'))
print(double_letters('hello!?!?!?!'))
print(double_letters('hello!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!?!?!?!?!?!?!?!?!?!'))
print(double_letters('hello!?!?!?!?!?!