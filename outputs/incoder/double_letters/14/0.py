
def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    double_letters_string = ''
    for char in string:
        if char.isdigit():
            double_letters_string += char*2
        elif char.isalpha():
            double_letters_string += char*3
        else:
            double_letters_string += char
    return double_letters_string

# Test Cases
print(double_letters('hello'))
print(double_letters('hello123'))
print(double_letters('hello123!'))
print(double_letters('hello123!@'))
print(double_letters('hello123!@#'))
print(double_letters('hello123!@#%'))
print(double_letters('hello123!@#%^'))
print(double_letters('hello123!@#%^&'))
print(double_letters('hello123!@#%^&*'))
print(double_letters('hello123!@#%^&*()'))
print(double_letters('hello123!@#%^&*()[]'))
print(double_letters('hello123!@#%^&*()[]{}'))
print(double_letters('hello123!@#%^&*()[]{}<>'))
print(double_letters('hello123!@#%^&*()[]{}<>:'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\/'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//.'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//..'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../.'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../..'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../..\\'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../..\\/'))
print(double_letters('hello123!@#%^&*()[]{}<>:\\//../..\\//'))
