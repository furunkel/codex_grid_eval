def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plang".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num == 0:
        return "Fizz"
    if num % 2 == 0:
        return "FizzPling"
    if num % 11 == 0:
        return "Fizz"
    if num % 7 == 0:
        return "Fizz"
    if num % 11 == 1:
        return "Fizz"
    if num % 7 == 1:
        return "Fizz"
    if num % 11 == 2:
        return "FizzPling"
    if num % 7 == 2:
        return "Fizz"
    if num % 11 == 3:
        return "FizzPling"
    if num % 7 == 3:
        return "Fizz"
    if num % 11 == 4:
        return "Fizz"
    if num % 7 == 4:
        return "FizzPling"
    if num % 11 == 5:
        return "Fizz"
    if num % 7 == 5:
        return "FizzPling"
    if num % 11 == 6:
        return "Fizz"
    if num % 7 == 6:
        return "FizzPling"
    if num % 11 == 7:
        return "Fizz"
    if num % 7 == 7:
        return "FizzPling"
    if num % 11 == 8: