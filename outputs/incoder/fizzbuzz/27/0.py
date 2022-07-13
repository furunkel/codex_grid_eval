
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 17 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 17 == 0:
        return "Buzz"
    else:
        return num


def fizzbuzz_with_if_statement(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 17 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 17 == 0:
        return "Buzz"
    else:
        return num


def fizzbuzz_with_ternary_operator(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    return num % 3 == 0 and num % 17 == 0 \
        ? "FizzBuzz" \
        : num % 3 == 0 \
            ? "Fizz" \
            : num % 17 == 0 \
                ? "Buzz" \
                : num


def fizzbuzz_with_ternary_operator2(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    return num % 3 == 0 and num % 17 == 0 \
        ? "FizzBuzz" \
        : num % 3 == 0 \
            ? "Fizz" \
            : num % 17 == 0 \
                ? "Buzz" \
                : num


def fizzbuzz_with_ternary_operator3(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    return num % 3 == 0 and num % 17 == 0 \
        ? "FizzBuzz" \
        : num % 3 == 0 \
            ? "Fizz" \
            : num % 17 == 0 \
                ? "Bu