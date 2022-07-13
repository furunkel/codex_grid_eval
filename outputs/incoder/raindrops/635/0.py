
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Buzz".
    39 has both 13 and 3 as factors, but not 11, so the result would be "PlangPling".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num == 3:
        return "3"
    if num == 4:
        return "4"
    if num == 5:
        return "5"
    if num == 6:
        return "6"
    if num == 7:
        return "7"
    if num == 8:
        return "8"
    if num == 9:
        return "9"
    if num == 10:
        return "Buzz"
    if num == 11:
        return "Pling"
    if num == 12:
        return "Plang"
    if num == 13:
        return "PlingPlang"
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 11 == 0:
                return "Buzz"
            else:
                return "Plang"
        else:
            if num % 13 == 0:
                return "Pling"
            else:
                return "PlangPling"
    else:
        if num % 3 == 0:
            if num % 11 == 0:
                return "Pling"
            else:
                return "Plang"
        else:
            if num % 13 == 0:
                return "Plang"
            else:
                return "PlingPlang"


def fibonacci(num):
    """
    Your task is to convert a number into a string that contains the Fibonacci sequence
    corresponding to the given number.

    Fibonacci sequences are sequences of numbers that grow very rapidly and are often used to represent sequences of numbers.
    For example, fibonacci(0) returns "0", fibonacci(1) returns "1", fibonacci(2) returns "1", and so on.

    Your task is to convert a number into a string that contains the Fibonacci sequence
    corresponding to the given number.

    Fibonacci sequences are sequences of numbers that grow very rapidly and are often used to represent sequences of numbers.
    For example, fibonacci(0) returns "0", fibonacci(1) returns "1", fibonacci(2) returns "1", and so on.

    Your task is to convert a number into a string that contains the Fibonacci sequence
    corresponding to the given number.

    Fibonacci sequences are sequences of numbers that grow very rapidly and are often used to represent sequences of numbers.
    For example, fibonacci(0) returns "0", fibonacci(1) returns "1", fibonacci(2) returns "1", and so on.

    Your task is to convert a number into a string that contains the Fibonacci sequence
    corresponding to the given 