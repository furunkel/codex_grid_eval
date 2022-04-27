
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of 3 (instead of the number),
        "FizzBuzz" for multiples of both 4 and 3  (instead of the number),
        the number itself otherwise.
    """
    if num % 4 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 4 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_list(n):
    """
    Given a number n, this function returns a list of numbers from 1 to n,
    where each number is replaced by "Fizz", "Buzz", "FizzBuzz", or the number itself
    as described in the fizzbuzz function.
    """
    return [fizzbuzz(i) for i in range(1, n+1)]

def fizzbuzz_dict(n):
    """
    Given a number n, this function returns a dictionary of numbers from 1 to n,
    where each number is replaced by "Fizz", "Buzz", "FizzBuzz", or the number itself
    as described in the fizzbuzz function.
    """
    return {i: fizzbuzz(i) for i in range(1, n+1)}

def fizzbuzz_dict_alt(n):
    """
    Given a number n, this function returns a dictionary of numbers from 1 to n,
    where each number is replaced by "Fizz", "Buzz", "FizzBuzz", or the number itself
    as described in the fizzbuzz function.
    """
    return dict(zip(range(1, n+1), [fizzbuzz(i) for i in range(1, n+1)]))

def fizzbuzz_dict_alt2(n):
    """
    Given a number n, this function returns a dictionary of numbers from 1 to n,
    where each number is replaced by "Fizz", "Buzz", "FizzBuzz", or the number itself
    as described in the fizzbuzz function.
    """
    return dict(enumerate(fizzbuzz_list(n), start=1))

def fizzbuzz_dict_alt3(n):
    """
    Given a number n, this function returns a dictionary of numbers from 1 to n,
    where each number is replaced by "Fizz