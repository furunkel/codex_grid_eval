
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 11, so the result would be "PlangPling".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Pling"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 7
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 17.
    You do not need to worry about numbers like 0 or 1.
    You do not need to worry about numbers like 6 or 8.
    You do not need to worry about numbers like 9 or 11.
    You do not need to worry about numbers like 19 or 20.
    You do not need to worry about numbers like 100 or 200.
    You do not need to worry about numbers like 300 or 400.
    You do not need to worry about numbers like 500 or 600.
    You do not need to worry about numbers like 700 or 800.
    You do not need to worry about numbers like 900 or 1000.
    You do not need to worry about numbers like 1100 or 1200.
    You do not need to worry about numbers like 1300 or 1400.
    You do not need to worry about numbers like 1500 or 1600.
    You do not need to worry about numbers like 1700 or 1800.
    You do not need to worry about numbers like 1900 or 2000.
    You do not need to worry about numbers like 2100 or 2200.
    You do not need to worry about numbers like 2300 or 2400.
    You do not need to worry about numbers like 2500 or 2600.
    You do not need to worry about numbers like 2700 or 2800.
    You do not need to worry about numbers like 2900 or 3000.
    You do not need to worry about numbers like 3100 or 3200.
    You do not need to worry about numbers like 3300 or 3400.
    You do not need to worry about numbers like 3500 or 3600.
    You do not need to worry about numbers like 3700 or 3800.
    You do not need to worry about numbers like 3900 or 4000.
    You do not need to worry about numbers like 4100 or 4200.
    You do not need to worry about numbers like 4300 or 4400.
    You do not need to worry about numbers like 4500 or 4600.
    