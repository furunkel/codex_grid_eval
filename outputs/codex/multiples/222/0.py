
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 9, we get 2, 4, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 65.
    Return the sum of all the multiples of 2 or 9 below 1000.
    """    
    return sum([x for x in range(1000) if x % 2 == 0 or x % 9 == 0])

def multiples_of_3_and_5():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

def even_fibonacci_numbers():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    return sum([x for x in fib if x % 2 == 0])

def largest_prime_factor():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

def largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if str(x * y) == str(x * y)[::-1]])

def smallest_