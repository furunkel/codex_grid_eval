
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'Buzz'
    elif num == 11:
        return 'Plong'
    elif num == 12:
        return 'Fizz'
    else:
        factors = []
        factors.append(num)
        while num != 1:
            factors.append(num % 10)
            num = num // 10
        factors.append(num)
        factors.sort()
        result = ''
        for factor in factors:
            if factor % 13 == 0:
                result += 'Fizz'
            elif factor % 3 == 0:
                result += 'Buzz'
            elif factor % 11 == 0:
                result += 'Plong'
            else:
                result += str(factor)
        return result


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz, Fizz, or Buzz.
    You will need to use an if statement to determine which word to use based on the number's value.

    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's value.
    You will need to use an if statement to determine which word to use based on the number's 