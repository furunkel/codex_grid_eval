
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of twenty-three (instead of the number),
        "FizzBuzz" for multiples of both 4 and twenty-three  (instead of the number),
        the number itself otherwise.
    """
    if num % 4 == 0 and num % 23 == 0:
        return "FizzBuzz"
    elif num % 4 == 0:
        return "Fizz"
    elif num % 23 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function calls the fizzbuzz function for each number from 1 to 100.
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()