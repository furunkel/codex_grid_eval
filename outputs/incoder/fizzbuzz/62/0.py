
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of twenty-three (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and twenty-three  (instead of the number),
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

# Test
print(fizzbuzz(15))
print(fizzbuzz(30))
print(fizzbuzz(45))
print(fizzbuzz(50))
print(fizzbuzz(100))
print(fizzbuzz(150))
print(fizzbuzz(250))
print(fizzbuzz(350))
print(fizzbuzz(400))
print(fizzbuzz(500))
print(fizzbuzz(600))
print(fizzbuzz(700))
print(fizzbuzz(800))
print(fizzbuzz(900))
print(fizzbuzz(1000))
print(fizzbuzz(1100))
print(fizzbuzz(1200))
print(fizzbuzz(1300))
print(fizzbuzz(1400))
print(fizzbuzz(1500))
print(fizzbuzz(1600))
print(fizzbuzz(1700))
print(fizzbuzz(1800))
print(fizzbuzz(1900))
print(fizzbuzz(2000))
print(fizzbuzz(2100))
print(fizzbuzz(2200))
print(fizzbuzz(2300))
print(fizzbuzz(2400))
print(fizzbuzz(2500))
print(fizzbuzz(2600))
print(fizzbuzz(2700))
print(fizzbuzz(2800))
print(fizzbuzz(2900))
print(fizzbuzz(3000))
print(fizzbuzz(3100))
print(fizzbuzz(3200))
print(fizzbuzz(3300))
print(fizzbuzz(3400))
print(fizzbuzz(3500))
print(fizzbuzz(3600))
print(fizzbuzz(3700))
print(fizzbuzz(3800))
print(fizzbuzz(3900))
print(fizzbuzz(4000))
print(fizzbuzz(4100))
print(fizzbuzz(4200))
print(fizzbuzz(4300))
print(fizzbuzz(4400))
print(fizzbuzz(450))
print(fizzbuzz(460))
