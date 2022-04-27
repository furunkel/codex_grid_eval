
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 3 (instead of the number),
        "Buzz" for multiples of twenty-three (instead of the number),
        "FizzBuzz" for multiples of both 3 and twenty-three  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 23 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 23 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    replacing multiples of 3 with "Fizz", multiples of 23 with "Buzz",
    and multiples of both 3 and 23 with "FizzBuzz".
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()