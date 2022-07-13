
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 5, 3 or 2 below 124.
    """    
    return reduce(lambda x, y: x * y, set(range(2, 124, 2) + range(3, 124, 3) + range(5, 124, 5)))

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.
    Return the sum of the squares of the first one hundred natural numbers.
    """
    return sum(map(lambda x: x ** 2, range(1, 101)))

def square_of_sum():
    """
    The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    Return the square of the sum of the first one hundred natural numbers.
    """
    return sum(range(1, 101)) ** 2

def difference_of_squares():
    """
    The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Return the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return square_of_sum() - sum_of_squares()

def sum_of_primes():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Return the sum of all the primes below two million.
    """
    return sum(primes(2000000))

def largest_product_in_series():
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744