
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 11 (instead of the number),
        "FizzBuzz" for multiples of both three and 11  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 11 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Buzz"
    else:
        return str(num)


# Write a function that takes a list and returns a new list with only the unique elements.
def unique_list(lst):
    """
    Given a list, this function returns a new list with only unique elements.
    """
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# Write a function that takes a list and returns a new list with only the elements that appear more than once.
def repeated_list(lst):
    """
    Given a list, this function returns a new list with only elements that appear more than once.
    """
    repeated_list = []
    for item in lst:
        if lst.count(item) > 1:
            repeated_list.append(item)
    return repeated_list


# Write a function that takes a list and returns a new list with only the elements that appear exactly once.
def unique_and_repeated_list(lst):
    """
    Given a list, this function returns a new list with only elements that appear exactly once.
    """
    unique_and_repeated_list = []
    for item in lst:
        if lst.count(item) == 1:
            unique_and_repeated_list.append(item)
    return unique_and_repeated_list


# Write a function that takes a list and returns a new list with only the elements that appear less than once.
def repeated_and_unique_list(lst):
    """
    Given a list, this function returns a new list with only elements that appear less than once.
    """
    repeated_and_unique_list = []
    for item in lst:
        if lst.count(item) < 1:
            repeated_and_unique_list.append(item)
    return repeated_and_unique_list


# Write a function that takes a list and returns a new list with only the elements that appear exactly once and are less than the given number.
def unique_and_repeated_less_than(lst):
    """
    Given a list, this function returns a new list with only elements that appear exactly once and are less than the given number.
    """
    unique_and_repeated_less_than_list = []
    for item in lst:
        if lst.count(item) == 1 and item < 3:
            unique_and_repeated_less_than_list.append(item)
    return unique_and_repeated_less_than_list


# Write a function that takes a list and returns a new list with only the elements that appear less than once and are less than the given number.
def repeated_and_unique_less_than(lst):
    """
    Given a list, this function returns a new list with only elements that appear less than once and are less than the given number.
    """
    repeated_and_unique_less_than_list = []
    for item in lst:
        if 