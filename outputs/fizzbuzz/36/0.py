
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of five (instead of the number),
        "Buzz" for multiples of 23 (instead of the number),
        "FizzBuzz" for multiples of both five and 23  (instead of the number),
        the number itself otherwise.
    """
    if num % 5 == 0 and num % 23 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Fizz"
    elif num % 23 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    replacing multiples of five with "Fizz",
    multiples of 23 with "Buzz",
    and multiples of both five and 23 with "FizzBuzz".
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()