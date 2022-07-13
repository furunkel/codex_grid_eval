
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 2, 3 or 5 below 600.
    """    
    return reduce(lambda x, y: x * y, set(range(2, 600, 2) + range(3, 600, 3) + range(5, 600, 5)))

def sum_of_squares():
    """
    The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.
    Return the sum of the squares of the first 100 natural numbers.
    """
    return sum(map(lambda x: x ** 2, range(1, 101)))

def square_of_sum():
    """
    The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    Return the square of the sum of the first 100 natural numbers.
    """
    return sum(range(1, 101)) ** 2

def difference_of_squares():
    """
    The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Return the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.
    """
    return square_of_sum() - sum_of_squares()

def nth_prime(n):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    Return the nth prime number.
    """
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 2
    return primes[-1]

def largest_prime_factor(n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    Return the largest prime factor of 600851475143.
    """
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

def largest_palindrome_product():
    """
   