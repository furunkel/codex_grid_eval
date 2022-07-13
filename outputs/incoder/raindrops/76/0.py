
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plang".
    15 has both 3 and 5 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return 'Fizz'
    elif num == 5:
        return 'Pling'
    elif num == 11:
        return 'Plang'
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if len(factors) == 0:
            return str(num)
        elif len(factors) == 1:
            return str(num) + str(factors[0])
        else:
            return str(num) + str(factors[0]) + str(factors[1])

# def raindrops(num):
#     """
#     Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
#     A factor is a number that evenly divides into another number, leaving no remainder.
#     The simplest way to test if one number is a factor of another is to use the modulo operation.

#     The rules of raindrops are that if a given number:

#     has 3 as a factor, add 'Fizz' to the result.
#     has 5 as a factor, add 'Pling' to the result.
#     has 11 as a factor, add 'Plang' to the result.
#     does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

#     Examples:
#     22 has 11 as a factor, but not 3 or 5, so the result would be "Plang".
#     15 has both 3 and 5 as factors, but not 11, so the result would be "FizzPling".
#     2 is not factored by 3, 5, or 11, so the result would be "2".
#     """
#     if num == 0:
#         return '0'
#     elif num == 1:
#         return '1'
#     elif num == 2:
#         return '2'
#     elif num == 3:
#         return 'Fizz'
#     elif num == 5:
#         return 'Pling'
#     elif num == 11:
#         return 'Plang'
#     else:
#         factors = []
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 factors.append(i)
#         if len(factors) == 0:
#             return str(num)
#         elif len(factors) == 1:
#             return str(num) + str(factors[0])
#         else:
#             return str(num) + str(factors[0]) + str(factors[1])

# def raindrops(num):
#     """
#     Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
#     A factor is a number that evenly divides into another number, leaving no remainder.
#     The simplest way to test if one number is a factor of another is to use the modulo operation.

#     The rules of raindrop