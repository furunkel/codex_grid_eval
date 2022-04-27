
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of seventeen (instead of the number),
        "Buzz" for multiples of 3 (instead of the number),
        "FizzBuzz" for multiples of both seventeen and 3  (instead of the number),
        the number itself otherwise.
    """
    if num % 17 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 17 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 100,
    replacing multiples of seventeen with "Fizz",
    multiples of 3 with "Buzz",
    multiples of both seventeen and 3 with "FizzBuzz",
    and the number itself otherwise.
    """
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()