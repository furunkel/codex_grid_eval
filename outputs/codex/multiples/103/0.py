
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The product of these multiples is 3456.
    Return the product of all the multiples of 2 or 9 below 197.
    """    
    return reduce(lambda x, y: x * y, [x for x in range(1, 197) if x % 2 == 0 or x % 9 == 0])

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.
    Return the sum of the squares of the first 197 natural numbers.
    """
    return reduce(lambda x, y: x + y, [x ** 2 for x in range(1, 197)])

def square_of_sum():
    """
    The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    Return the square of the sum of the first 197 natural numbers.
    """
    return reduce(lambda x, y: x + y, range(1, 197)) ** 2

def difference():
    """
    The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Return the difference between the sum of the squares of the first 197 natural numbers and the square of the sum.
    """
    return square_of_sum() - sum_of_squares()

def main():
    print multiples()
    print sum_of_squares()
    print square_of_sum()
    print difference()

if __name__ == '__main__':
    main()