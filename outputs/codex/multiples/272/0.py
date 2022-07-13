
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 200.
    """    
    return sum([x for x in range(200) if x % 2 == 0 or x % 3 == 0 or x % 5 == 0])

def fibonacci():
    """
    The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    fib = [1, 1]
    while len(str(fib[-1])) < 1000:
        fib.append(fib[-1] + fib[-2])
    return len(fib)

def palindrome():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if str(i * j) == str(i * j)[::-1]:
                palindromes.append(i * j)
    return max(palindromes)

def smallest_multiple():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    i = 20
    while True:
        if all([i % x == 0 for x in range(1, 21)]):
            return i
        i += 20

def sum_square_difference():
    """