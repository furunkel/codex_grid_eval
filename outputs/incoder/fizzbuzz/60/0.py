
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 23 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 23  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


# Write a function that takes a list and returns a new list with only unique elements.
def unique_list(lst):
    """
    Given a list, this function returns a new list with only unique elements.
    """
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_upper(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    upper_str = str.upper()
    return upper_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_lower(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    lower_str = str.lower()
    return lower_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_title(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    title_str = str.title()
    return title_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_upper(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    upper_str = str.upper()
    return upper_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_lower(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    lower_str = str.lower()
    return lower_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_title(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
    title_str = str.title()
    return title_str


# Write a function that takes a string and returns a new string with all lowercase letters replaced by uppercase letters.
def to_upper(str):
    """
    Given a string, this function returns a new string with all lowercase letters replaced by uppercase letters.
    """
