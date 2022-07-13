
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 3 or 5 below 500.
    """    
    sum = 0
    for i in range(1, 501):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# print multiples()
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes():
    """
    Find the sum of all the primes below two million.
    """
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

# print primes()
</cell>
<text>
Problem 8
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    sum = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            if i * j == rev(i * j):
                sum += i * j
    return sum

# print palindromes()
</cell>
<text>
Problem 9
A palindromic number reads the same both ways. The largest palindrome made from the product of two 3-digit numbers is 906609 = 906609 x 996609.
Find the largest palindrome made from the product of two 4-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 4-digit numbers.
    """
    sum = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            if i * j == rev(i * j):
                sum += i * j
    return sum

# print palindromes()
</cell>
<text>
Problem 10
A palindromic number reads the same both ways. The largest palindrome made from the product of two 4-digit numbers is 906609 = 906609 x 996609.
Find the largest palindrome made from the product of two 5-digit numbers.


</text>
<cell>
def palindromes():
    """
    Find the largest palindrome made from the product of two 5-digit numbers.
    """
    sum = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            if i * j == rev(i * j):
                sum += i * j
    return sum

# print palindromes()
</cell>
<text>