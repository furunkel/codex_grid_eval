
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 5, so the result would be "2".
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
    elif num == 13:
        return 'FizzBuzz'
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if len(factors) == 0:
            return str(num)
        elif len(factors) == 1:
            return str(factors[0])
        else:
            factors.sort()
            factors.reverse()
            factors = factors[:len(factors)-1]
            factors.insert(0, 'Fizz')
            factors.insert(1, 'Buzz')
            factors.insert(2, 'Plong')
            factors.insert(3, 'FizzBuzz')
            factors.insert(4, 'BuzzPlong')
            factors.insert(5, 'FizzBuzzPlong')
            factors.insert(6, 'BuzzFizz')
            factors.insert(7, 'BuzzBuzz')
            factors.insert(8, 'BuzzBuzzPlong')
            factors.insert(9, 'BuzzFizzBuzz')
            factors.insert(10, 'BuzzBuzzFizz')
            factors.insert(11, 'BuzzBuzzBuzz')
            factors.insert(12, 'BuzzFizzBuzzPlong')
            factors.insert(13, 'BuzzFizzBuzzFizz')
            factors.insert(14, 'BuzzBuzzFizzBuzz')
            factors.insert(15, 'BuzzBuzzFizzBuzzPlong')
            factors.insert(16, 'BuzzBuzzFizzBuzzFizz')
            factors.insert(17, 'BuzzBuzzFizzBuzzBuzz')
            factors.insert(18, 'BuzzBuzzFizzBuzzBuzzPlong')
            factors.insert(19, 'BuzzBuzzFizzBuzzBuzzFizz')
            factors.insert(20, 'BuzzBuzzFizzBuzzBuzzBuzz')
            factors.insert(21, 'BuzzBuzzFizzBuzzBuzzBuzzPlong')
            factors.