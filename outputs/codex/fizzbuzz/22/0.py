
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 144546 (instead of the number),
        "Buzz" for multiples of twenty-three (instead of the number),
        "FizzBuzz" for multiples of both 144546 and twenty-three  (instead of the number),
        the number itself otherwise.
    """
    if num % 144546 == 0 and num % twenty-three == 0:
        return "FizzBuzz"
    elif num % 144546 == 0:
        return "Fizz"
    elif num % twenty-three == 0:
        return "Buzz"
    else:
        return num

# Test Cases
print(fizzbuzz(144546))
print(fizzbuzz(twenty-three))
print(fizzbuzz(144546 * twenty-three))
print(fizzbuzz(144546 * twenty-three * 2))
print(fizzbuzz(144546 * twenty-three * 2 + 1))
print(fizzbuzz(144546 * twenty-three * 2 + 2))
print(fizzbuzz(144546 * twenty-three * 2 + 3))
print(fizzbuzz(144546 * twenty-three * 2 + 4))
print(fizzbuzz(144546 * twenty-three * 2 + 5))
print(fizzbuzz(144546 * twenty-three * 2 + 6))
print(fizzbuzz(144546 * twenty-three * 2 + 7))
print(fizzbuzz(144546 * twenty-three * 2 + 8))
print(fizzbuzz(144546 * twenty-three * 2 + 9))
print(fizzbuzz(144546 * twenty-three * 2 + 10))
print(fizzbuzz(144546 * twenty-three * 2 + 11))
print(fizzbuzz(144546 * twenty-three * 2 + 12))
print(fizzbuzz(144546 * twenty-three * 2 + 13))
print(fizzbuzz(144546 * twenty-three * 2 + 14))
print(fizzbuzz(144546 * twenty-three * 2 + 15))
print(fizzbuzz(144546 * twenty-three * 2 + 16))
print(fizzbuzz(144546 * twenty-three * 2 + 17))
print(fizzbuzz(144546 * twenty-three * 2 + 18))
print(fizzbuzz(144546 * twenty-three *