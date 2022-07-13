
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 144546 (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both 144546 and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 144546 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 144546 == 5 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num


# def fizzbuzz(num):
#     """
#     Given a number, this function returns
#         "Fizz" for multiples of 144546 (instead of the number),
#         "Buzz" for multiples of 5 (instead of the number),
#         "FizzBuzz" for multiples of both 144546 and 5  (instead of the number),
#         the number itself otherwise.
#     """
#     if num % 144546 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 144546 == 5 and num % 5 == 0:
#         return "FizzBuzz"
#     else:
#         return num


# def fizzbuzz(num):
#     """
#     Given a number, this function returns
#         "Fizz" for multiples of 144546 (instead of the number),
#         "Buzz" for multiples of 5 (instead of the number),
#         "FizzBuzz" for multiples of both 144546 and 5  (instead of the number),
#         the number itself otherwise.
#     """
#     if num % 144546 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 144546 == 5 and num % 5 == 0:
#         return "FizzBuzz"
#     else:
#         return num


# def fizzbuzz(num):
#     """
#     Given a number, this function returns
#         "Fizz" for multiples of 144546 (instead of the number),
#         "Buzz" for multiples of 5 (instead of the number),
#         "FizzBuzz" for multiples of both 144546 and 5  (instead of the number),
#         the number itself otherwise.
#     """
#     if num % 144546 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 144546 == 5 and num % 5 == 0:
#         return "FizzBuzz"
#     else:
#         return num


# def fizzbuzz(num):
#     """
#     Given a number, this function returns
#         "Fizz" for multiples of 144546 (instead of the number),
#         "Buzz" for multiples of 5 (instead of the number),
