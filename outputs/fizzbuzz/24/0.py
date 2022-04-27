
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both three and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_list(nums):
    """
    Given a list of numbers, this function returns a list of strings
    where each string is the result of applying fizzbuzz to the corresponding
    number in the list.
    """
    return [fizzbuzz(num) for num in nums]

def fizzbuzz_dict(nums):
    """
    Given a list of numbers, this function returns a dictionary
    where the keys are the numbers and the values are the result of applying
    fizzbuzz to the corresponding number in the list.
    """
    return {num: fizzbuzz(num) for num in nums}

def fizzbuzz_dict_2(nums):
    """
    Given a list of numbers, this function returns a dictionary
    where the keys are the numbers and the values are the result of applying
    fizzbuzz to the corresponding number in the list.
    """
    return dict(zip(nums, fizzbuzz_list(nums)))

def fizzbuzz_dict_3(nums):
    """
    Given a list of numbers, this function returns a dictionary
    where the keys are the numbers and the values are the result of applying
    fizzbuzz to the corresponding number in the list.
    """
    return dict(map(lambda num: (num, fizzbuzz(num)), nums))

def fizzbuzz_dict_4(nums):
    """
    Given a list of numbers, this function returns a dictionary
    where the keys are the numbers and the values are the result of applying
    fizzbuzz to the corresponding number in the list.
    """
    return dict(map(lambda num: (num, fizzbuzz(num)), nums))

def fizzbuzz_dict_5(nums):
    """
    Given a list of numbers, this function returns a dictionary
    where