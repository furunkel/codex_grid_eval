
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of 11 (instead of the number),
        "FizzBuzz" for multiples of both 4 and 11  (instead of the number),
        the number itself otherwise.
    """
    if num % 4 == 0 and num % 11 == 0:
        return "FizzBuzz"
    elif num % 4 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    replacing multiples of 4 with "Fizz", multiples of 11 with "Buzz",
    and multiples of both 4 and 11 with "FizzBuzz".
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()