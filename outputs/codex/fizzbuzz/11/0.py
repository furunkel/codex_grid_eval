
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both 4 and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 4 == 0 and num % 17 == 0:
        return "FizzBuzz"
    elif num % 4 == 0:
        return "Fizz"
    elif num % 17 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_list(nums):
    """
    Given a list of numbers, this function returns a list of the same length,
    where each element is the result of applying fizzbuzz to the corresponding
    element of the input list.
    """
    return [fizzbuzz(num) for num in nums]

def fizzbuzz_dict(nums):
    """
    Given a list of numbers, this function returns a dictionary where the keys
    are the numbers in the input list, and the values are the result of applying
    fizzbuzz to the corresponding number.
    """
    return {num: fizzbuzz(num) for num in nums}

def fizzbuzz_set(nums):
    """
    Given a list of numbers, this function returns a set of the results of
    applying fizzbuzz to the numbers in the input list.
    """
    return {fizzbuzz(num) for num in nums}

def fizzbuzz_tuple(nums):
    """
    Given a list of numbers, this function returns a tuple of the results of
    applying fizzbuzz to the numbers in the input list.
    """
    return tuple(fizzbuzz(num) for num in nums)

def fizzbuzz_generator(nums):
    """
    Given a list of numbers, this function returns a generator of the results of
    applying fizzbuzz to the numbers in the input list.
    """
    for num in nums:
        yield fizzbuzz(num)

def fizzbuzz_map(nums):
    """
    Given a list of numbers, this function returns a map object of the results of
    applying fizzbuzz to the numbers in the input list.
    """
    return map(fizzbuzz, nums)

def fizzbuzz_filter(nums):