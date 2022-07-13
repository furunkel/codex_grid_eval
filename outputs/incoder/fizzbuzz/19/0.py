
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 144546 (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both 144546 and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 144546 == 0 and num % 17 == 0:
        return "FizzBuzz"
    elif num % 144546 == 0:
        return "Fizz"
    elif num % 17 == 0:
        return "Buzz"
    else:
        return num


# Write a function that takes a list and returns a new list with only the numbers that are multiples of 3 or 5.
def multiples_of_3_or_5(lst):
    """
    Given a list, this function returns a new list with only the numbers that are multiples of 3 or 5.
    """
    lst2 = []
    for i in lst:
        if i % 3 == 0 or i % 5 == 0:
            lst2.append(i)
    return lst2


# Write a function that takes a list and returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100.
def multiples_of_3_or_5_and_less_than_100(lst):
    """
    Given a list, this function returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100.
    """
    lst2 = []
    for i in lst:
        if i % 3 == 0 or i % 5 == 0 and i < 100:
            lst2.append(i)
    return lst2


# Write a function that takes a list and returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100 and are greater than 0.
def multiples_of_3_or_5_and_less_than_100_and_greater_than_0(lst):
    """
    Given a list, this function returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100 and are greater than 0.
    """
    lst2 = []
    for i in lst:
        if i % 3 == 0 or i % 5 == 0 and i < 100 and i > 0:
            lst2.append(i)
    return lst2


# Write a function that takes a list and returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100 and are greater than 0 and are less than 20.
def multiples_of_3_or_5_and_less_than_100_and_greater_than_0_and_less_than_20(lst):
    """
    Given a list, this function returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100 and are greater than 0 and are less than 20.
    """
    lst2 = []
    for i in lst:
        if i % 3 == 0 or i % 5 == 0 and i < 100 and i > 0:
            if i < 20:
                lst2.append(i)
    return lst2


# Write a function that takes a list and returns a new list with only the numbers that are multiples of 3 or 5 and are less than 100 and are greater than 0 and are less than 20.
def multiples_of_3_or_5_and_less_than_100_and_greater_than_0_and_less_than_20(lst):
    """
    Given 