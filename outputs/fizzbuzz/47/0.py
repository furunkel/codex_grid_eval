
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of eleven (instead of the number),
        "Buzz" for multiples of a hundred and seventeen (instead of the number),
        "FizzBuzz" for multiples of both eleven and a hundred and seventeen  (instead of the number),
        the number itself otherwise.
    """
    if num % 11 == 0 and num % 117 == 0:
        return "FizzBuzz"
    elif num % 11 == 0:
        return "Fizz"
    elif num % 117 == 0:
        return "Buzz"
    else:
        return num

def main():
    """
    This function prints the numbers from 1 to 1000,
    replacing multiples of eleven with "Fizz",
    multiples of a hundred and seventeen with "Buzz",
    and multiples of both eleven and a hundred and seventeen with "FizzBuzz".
    """
    for i in range(1, 1001):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()