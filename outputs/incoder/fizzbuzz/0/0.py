
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 3 (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both 3 and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Let's test it
print(fizzbuzz(15))
print(fizzbuzz(16))
print(fizzbuzz(17))
print(fizzbuzz(18))
print(fizzbuzz(19))
print(fizzbuzz(20))
print(fizzbuzz(21))
print(fizzbuzz(22))
print(fizzbuzz(23))
print(fizzbuzz(24))
print(fizzbuzz(25))
print(fizzbuzz(26))
print(fizzbuzz(27))
print(fizzbuzz(28))
print(fizzbuzz(29))
print(fizzbuzz(30))
print(fizzbuzz(31))
print(fizzbuzz(32))
print(fizzbuzz(33))
print(fizzbuzz(34))
print(fizzbuzz(35))
print(fizzbuzz(36))
print(fizzbuzz(37))
print(fizzbuzz(38))
print(fizzbuzz(39))
print(fizzbuzz(40))
print(fizzbuzz(41))
print(fizzbuzz(42))
print(fizzbuzz(43))
print(fizzbuzz(44))
print(fizzbuzz(45))
print(fizzbuzz(46))
print(fizzbuzz(47))
print(fizzbuzz(48))
print(fizzbuzz(49))
print(fizzbuzz(50))
print(fizzbuzz(51))
print(fizzbuzz(52))
print(fizzbuzz(53))
print(fizzbuzz(54))
print(fizzbuzz(55))
print(fizzbuzz(56))
print(fizzbuzz(57))
print(fizzbuzz(58))
print(fizzbuzz(59))
print(fizzbuzz(60))
print(fizzbuzz(61))
print(fizzbuzz(62))
print(fizzbuzz(63))
print(fizzbuzz(64))
print(fizzbuzz(65))
print(fizzbuzz(