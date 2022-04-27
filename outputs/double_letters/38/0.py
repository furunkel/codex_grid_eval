
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    vowels = 'aeiouAEIOU'
    new_string = ''
    for char in string:
        if char == '!':
            new_string += '!!'
        elif char in vowels:
            new_string += char * 3
        else:
            new_string += char
    return new_string

def double_letters_test():
    print(double_letters('Hello World!'))
    print(double_letters('Hello World!!'))
    print(double_letters('Hello World!!!'))
    print(double_letters('Hello World!!!!'))
    print(double_letters('Hello World!!!!!'))
    print(double_letters('Hello World!!!!!!'))
    print(double_letters('Hello World!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!'))
    print(double_letters('Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'))
    print