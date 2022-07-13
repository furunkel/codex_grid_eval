
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Buzz".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    if num == 3:
        return '3'
    if num == 4:
        return '4'
    if num == 5:
        return '5'
    if num == 6:
        return '6'
    if num == 7:
        return '7'
    if num == 8:
        return '8'
    if num == 9:
        return '9'
    if num == 10:
        return 'Buzz'
    if num == 11:
        return 'Pling'
    if num == 12:
        return 'Plang'
    if num == 13:
        return 'PlingPlang'
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                return 'BuzzBuzz'
            else:
                return 'Buzz'
        else:
            if num % 5 == 0:
                return 'PlingBuzz'
            else:
                return 'Pling'
    else:
        if num % 3 == 0:
            if num % 5 == 0:
                return 'PlangBuzz'
            else:
                return 'Plang'
        else:
            if num % 5 == 0:
                return 'PlingPlang'
            else:
                return 'Pling'


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append the word 'Fizz' to the result, and for multiples of five (buzz), you append the word 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 20.
    You do not need to worry about negative numbers, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of both three and five, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of both three and five, but also multiples of both three and five and so on, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of three or five, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of three or five, but also multiples of three or five and so on, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of three or five, but also multiples of three or five and so on, because they will always produce FizzBuzz.
    You do not need to worry about numbers that are multiples of three 