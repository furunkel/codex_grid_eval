
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of eleven (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both eleven and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num

# Now let's test our function
print(fizzbuzz(15))
print(fizzbuzz(17))
print(fizzbuzz(19))
print(fizzbuzz(25))
print(fizzbuzz(29))
print(fizzbuzz(33))
print(fizzbuzz(37))
print(fizzbuzz(41))
print(fizzbuzz(47))
print(fizzbuzz(53))
print(fizzbuzz(59))
print(fizzbuzz(65))
print(fizzbuzz(71))
print(fizzbuzz(77))
print(fizzbuzz(83))
print(fizzbuzz(89))
print(fizzbuzz(97))
print(fizzbuzz(103))
print(fizzbuzz(109))
print(fizzbuzz(113))
print(fizzbuzz(117))
print(fizzbuzz(121))
print(fizzbuzz(127))
print(fizzbuzz(131))
print(fizzbuzz(137))
print(fizzbuzz(141))
print(fizzbuzz(147))
print(fizzbuzz(151))
print(fizzbuzz(157))
print(fizzbuzz(161))
print(fizzbuzz(167))
print(fizzbuzz(171))
print(fizzbuzz(177))
print(fizzbuzz(181))
print(fizzbuzz(187))
print(fizzbuzz(191))
print(fizzbuzz(197))
print(fizzbuzz(201))
print(fizzbuzz(207))
print(fizzbuzz(211))
print(fizzbuzz(217))
print(fizzbuzz(221))
print(fizzbuzz(227))
print(fizzbuzz(231))
print(fizzbuzz(237))
print(fizzbuzz(241))
print(fizzbuzz(247))
print(fizzbuzz(251))
print(fizzbuzz(257))
print(fizzbuzz(261))
print(fizzbuzz(267))
print(fizzbuzz(271))
