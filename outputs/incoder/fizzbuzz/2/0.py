
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 3 (instead of the number),
        "Buzz" for multiples of 11 (instead of the number),
        "FizzBuzz" for multiples of both 3 and 11  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 11 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Buzz"
    else:
        return num


# Tests
def test_fizzbuzz():
    assert fizzbuzz(3) == "FizzBuzz"
    assert fizzbuzz(11) == "FizzBuzz"
    assert fizzbuzz(15) == "Buzz"
    assert fizzbuzz(21) == "Fizz"
    assert fizzbuzz(25) == "Buzz"
    assert fizzbuzz(29) == "Fizz"
    assert fizzbuzz(33) == "Fizz"
    assert fizzbuzz(37) == "Fizz"
    assert fizzbuzz(41) == "Buzz"
    assert fizzbuzz(43) == "Buzz"
    assert fizzbuzz(47) == "Buzz"
    assert fizzbuzz(51) == "Fizz"
    assert fizzbuzz(55) == "Fizz"
    assert fizzbuzz(59) == "Fizz"
    assert fizzbuzz(61) == "Fizz"
    assert fizzbuzz(65) == "Fizz"
    assert fizzbuzz(69) == "Fizz"
    assert fizzbuzz(71) == "Fizz"
    assert fizzbuzz(73) == "Fizz"
    assert fizzbuzz(77) == "Fizz"
    assert fizzbuzz(79) == "Fizz"
    assert fizzbuzz(83) == "Buzz"
    assert fizzbuzz(89) == "Buzz"
    assert fizzbuzz(97) == "Buzz"
    assert fizzbuzz(101) == "Fizz"
    assert fizzbuzz(103) == "Fizz"
    assert fizzbuzz(107) == "Fizz"
    assert fizzbuzz(109) == "Fizz"
    assert fizzbuzz(113) == "Fizz"
    assert fizzbuzz(127) == "Fizz"
    assert fizzbuzz(131) == "Fizz"
    assert fizzbuzz(137) == "Fizz"
    assert fizzbuzz(139) == "Fizz"
    assert fizzbuzz(141) == "Buzz"
    assert fizzbuzz(143) == "Buzz"
    assert fizzbuzz(147) == "Buzz"
    assert fizzbuzz(149) == "Buzz"
    assert fizzbuzz(15