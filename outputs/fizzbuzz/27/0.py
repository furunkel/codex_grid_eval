
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of three (instead of the number),
        "Buzz" for multiples of 17 (instead of the number),
        "FizzBuzz" for multiples of both three and 17  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 17 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 17 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    replacing multiples of three with the string "Fizz",
    multiples of 17 with the string "Buzz",
    and multiples of both three and 17 with the string "FizzBuzz".
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()