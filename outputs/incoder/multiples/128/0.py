
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5 or 3, we get 3, 5, 6, 9, 10 and 12. The sum of these multiples is 45.
    Return the sum of all the multiples of 5 or 3 below 124.
    """    
    
    sum = 0
    for i in range(1, 125):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 4
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_under_2million():
    """
    Find the sum of all the primes below two million.
    """
    
    sum = 0
    for i in range(2, 2000000):
        if isprime(i):
            sum += i
    return sum

print(primes_under_2million())
</cell>
<text>
Problem 5
A permutation is a special type of mathematical object that consists of two or more objects. For example, 3124 is one permutation of numbers 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def million_lexicographic_permutations():
    """
    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.
    """
    
    millionth_lexicographic_permutation = 0
    
    # Write your code here
    
    return millionth_lexicographic_permutation

print(million_lexicographic_permutations())
</cell>
<text>
Problem 6
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of the first six prime numbers.


</text>
<cell>
def primes_under_six():
    """
    Find the sum of the first six prime numbers.
    """
    
    sum = 0
    for i in range(2, 6):
        if isprime(i):
            sum += i
    return sum

print(primes_under_six())
</cell>
<text>
Problem 7
The sum of the first ten natural numbers is
\begin{equation}
  2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 +
  59 + 61 + 67 + 71 + 73 +
\end{equation}
Find the sum of all the first ten natural numbers.


</text>
<cell>
def first_ten_numbers():
    """
    Find the sum of all the first ten natural numbers.