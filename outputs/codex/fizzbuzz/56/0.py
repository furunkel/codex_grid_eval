
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of ninety-nine (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both ninety-nine and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 99 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 99 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    but for multiples of ninety-nine (instead of the number),
    "Buzz" for multiples of 5 (instead of the number),
    "FizzBuzz" for multiples of both ninety-nine and 5  (instead of the number),
    the number itself otherwise.
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()