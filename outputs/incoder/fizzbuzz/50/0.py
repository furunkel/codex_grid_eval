
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of seventeen (instead of the number),
        "Buzz" for multiples of 11 (instead of the number),
        "FizzBuzz" for multiples of both seventeen and 11  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Write a function that takes a list and a number as input
# and returns a list with the numbers in the list replaced by the numbers in the list multiplied by the number
def multiply_list(list_to_multiply, multiplier):
    """
    Given a list and a number, this function returns
        the list with the numbers in the list replaced by the numbers in the list multiplied by the number
    """
    multiplied_list = []
    for num in list_to_multiply:
        multiplied_list.append(num * multiplier)
    return multiplied_list

# Write a function that takes a list and a number as input
# and returns a list with the numbers in the list replaced by the numbers in the list divided by the number
def divide_list(list_to_divide, divisor):
    """
    Given a list and a number, this function returns
        the list with the numbers in the list replaced by the numbers in the list divided by the number
    """
    divided_list = []
    for num in list_to_divide:
        divided_list.append(num / divisor)
    return divided_list

# Write a function that takes a list and a number as input
# and returns a list with the numbers in the list replaced by the numbers in the list raised to the number
def raised_list(list_to_raise, power):
    """
    Given a list and a number, this function returns
        the list with the numbers in the list replaced by the numbers in the list raised to the number
    """
    raised_list = []
    for num in list_to_raise:
        raised_list.append(num ** power)
    return raised_list

# Write a function that takes a list and a number as input
# and returns a list with the numbers in the list replaced by the numbers in the list divided by the number
def divided_list(list_to_divide, divisor):
    """
    Given a list and a number, this function returns
        the list with the numbers in the list replaced by the numbers in the list divided by the number
    """
    divided_list = []
    for num in list_to_divide:
        divided_list.append(num / divisor)
    return divided_list

# Write a function that takes a list and a number as input
# and returns a list with the numbers in the list replaced by the numbers in the list raised to the number
def raised_list_2(list_to_raise, power):
    """
    Given a list and a number, this function returns
        the list with the numbers in the list replaced by the numbers in the list raised to the number
    """
    raised_list = []
    for num in list_to_raise:
        raised_list.append(num ** power)
    return raised_list

# Write a function that takes a 