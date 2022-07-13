
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The product of these multiples is 87091200.
    Return the product of all the multiples of 2, 3 or 5 below 1000.
    """    
    return reduce(lambda x, y: x * y, set(range(2, 1000, 2)) | set(range(3, 1000, 3)) | set(range(5, 1000, 5)))

def sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return sum(range(1, 101)) ** 2 - sum(map(lambda x: x ** 2, range(1, 101)))

def prime_10001():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    primes = [2]
    i = 3
    while len(primes) < 10001:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 2
    return primes[-1]

def largest_product_in_series():
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    series = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    1254069874715852386305071569329096329522744304