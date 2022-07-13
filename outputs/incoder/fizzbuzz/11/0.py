
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both 4 and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num

# Test Cases
print(fizzbuzz(15))
print(fizzbuzz(17))
print(fizzbuzz(19))
print(fizzbuzz(25))
print(fizzbuzz(30))
print(fizzbuzz(35))
print(fizzbuzz(40))
print(fizzbuzz(45))
print(fizzbuzz(50))
print(fizzbuzz(55))
print(fizzbuzz(60))
print(fizzbuzz(65))
print(fizzbuzz(70))
print(fizzbuzz(75))
print(fizzbuzz(80))
print(fizzbuzz(85))
print(fizzbuzz(90))
print(fizzbuzz(95))
print(fizzbuzz(100))
print(fizzbuzz(105))
print(fizzbuzz(110))
print(fizzbuzz(115))
print(fizzbuzz(120))
print(fizzbuzz(125))
print(fizzbuzz(130))
print(fizzbuzz(135))
print(fizzbuzz(140))
print(fizzbuzz(145))
print(fizzbuzz(150))
print(fizzbuzz(155))
print(fizzbuzz(160))
print(fizzbuzz(165))
print(fizzbuzz(170))
print(fizzbuzz(175))
print(fizzbuzz(180))
print(fizzbuzz(185))
print(fizzbuzz(190))
print(fizzbuzz(195))
print(fizzbuzz(200))
print(fizzbuzz(205))
print(fizzbuzz(210))
print(fizzbuzz(215))
print(fizzbuzz(220))
print(fizzbuzz(225))
print(fizzbuzz(230))
print(fizzbuzz(235))
print(fizzbuzz(240))
print(fizzbuzz(245))
print(fizzbuzz(250))
print(fizzbuzz(255))
print(fizzbuzz(260))
print(fizzbuzz(265))
print(fi