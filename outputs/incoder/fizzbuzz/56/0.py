
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# Tests
def test_fizzbuzz_1():
    assert fizzbuzz(1) == "1"


def test_fizzbuzz_2():
    assert fizzbuzz(2) == "2"


def test_fizzbuzz_3():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_4():
    assert fizzbuzz(4) == "Buzz"


def test_fizzbuzz_5():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_6():
    assert fizzbuzz(6) == "FizzBuzz"


def test_fizzbuzz_7():
    assert fizzbuzz(7) == "FizzBuzz"


def test_fizzbuzz_8():
    assert fizzbuzz(8) == "FizzBuzz"


def test_fizzbuzz_9():
    assert fizzbuzz(9) == "FizzBuzz"


def test_fizzbuzz_10():
    assert fizzbuzz(10) == "FizzBuzz"


def test_fizzbuzz_11():
    assert fizzbuzz(11) == "FizzBuzz"


def test_fizzbuzz_12():
    assert fizzbuzz(12) == "FizzBuzz"


def test_fizzbuzz_13():
    assert fizzbuzz(13) == "FizzBuzz"


def test_fizzbuzz_14():
    assert fizzbuzz(14) == "FizzBuzz"


def test_fizzbuzz_15():
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_16():
    assert fizzbuzz(16) == "FizzBuzz"


def test_fizzbuzz_17():
    assert fizzbuzz(17) == "FizzBuzz"


def test_fizzbuzz_18():
    assert fizzbuzz(18) == "FizzBuzz"


def test_fizzbuzz_19():
    assert fizzbuzz(19) == "FizzBuzz"


def test_fizzbuzz_20():
    assert fizzbuzz(20) == "FizzBuzz"


def test_fizzbuzz_21():
    assert fizzbuzz(21) == "FizzBuzz"


def test_fi