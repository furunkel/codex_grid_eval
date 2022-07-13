
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 13 or 17, we get  and 13. The sum of these multiples is 13.
    Return the sum of all the multiples of 13 or 17 below 197.
    """    
    
    sum = 0
    for i in range(1, 20):
        if i % 13 == 0 or i % 17 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 8
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


</text>
<cell>
def amicable(n):
    """
    d(n) is the sum of proper divisors of n (numbers less than n which divide evenly into n)
    """
    
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

print(amicable(10000))
</cell>
<text>
Problem 9
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    d(n) is the sum of proper divisors of n (numbers less than n which divide evenly into n)
    """
    
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

print(lexicographic_permutation(1000000))
</cell>
<text>
Problem 10
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


</text>
<cell>
def lexicographic_permutation(n):
    """
    d(n) is the sum of proper divisors of n (numbers less than n which divide 