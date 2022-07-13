
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5 or 3, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Return the sum of all the multiples of 5 or 3 below 600.
    """    
    sum = 0
    for x in range(600):
        if x % 5 == 0 or x % 3 == 0:
            sum += x
    return sum

# print multiples()
</cell>
<text>
Problem 8
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below(n):
    """
    Generate a list of primes below n.
    """
    primes = []
    for x in range(2, n):
        if n % x == 0:
            primes.append(x)
    return primes

def sum_of_primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    sum = 0
    for p in primes_below(n):
        sum += p
    return sum

# print sum_of_primes_below(2000000)
</cell>
<text>
Problem 9
The sum of the first ten natural numbers is,
1^1 + 2^2 + 3^3 + ... + 10^10.
The sum of the first ten natural numbers is,
1^1 + 2^2 + 3^3 + ... + 10^10.
The sum of the first ten natural numbers is,
1^1 + 2^2 + 3^3 + ... + 10^10.
Find the sum of all the first ten natural numbers below two million.


</text>
<cell>
def sum_of_first_ten_numbers(n):
    """
    Find the sum of all the first ten natural numbers below n.
    """
    sum = 0
    for x in range(1, 11):
        sum += x**x
    return sum

# print sum_of_first_ten_numbers(2000000)
</cell>
<text>
Problem 10
The sum of the first one hundred natural numbers is,
1^1 + 2^2 + 3^3 + ... + 100^100.
The sum of the first one hundred natural numbers is,
1^1 + 2^2 + 3^3 + ... + 100^100.
The sum of the first one hundred natural numbers is,
1^1 + 2^2 + 3^3 + ... + 100^100.
Find the sum of all the first one hundred natural numbers below two million.


</text>
<cell>
def sum_of_first_hundred_numbers(n):
    """
    Find the sum of all the first one hundred natural numbers below n.
    """
    sum = 0
    for x in range(1, 101):
        sum += x**x
    return sum

# print sum_of_first_hundred_numbers(2000000)
</cell>
<text>
Problem 11
A permutation is an ordered arrangement of objects. For example, 3124 is 