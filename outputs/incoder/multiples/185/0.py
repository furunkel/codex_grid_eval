
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 13 or 17, we get  and 13. The product of these multiples is 13.
    Return the product of all the multiples of 13 or 17 below 124.
    """    
    
    multiples = []
    
    for n in range(125, 1, -1):
        if n % 13 == 0 or n % 17 == 0:
            multiples.append(n)
            
    return multiples 
</cell>
<cell>
multiples()
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
    Sum of proper divisors of n
    """
    
    sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            sum += i
            
    return sum
</cell>
<cell>
amicable(10000)
</cell>
<text>
Problem 9
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


</text>
<cell>
def amicable(n):
    """
    Sum of proper divisors of n
    """
    
    sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            sum += i
            
    return sum
</cell>
<cell>
amicable(10000)
</cell>
<text>
Problem 10
A permutation is a special type of set which can contain repeated elements. A permutation is a special type of set which can contain repeated elements. A permutation is a special type of set which can contain repeated elements. A permutation is a special type of set which can contain repeated elements. A permutation is a special type of set which can contain repeated elements. A permutation is a special type of set which can contain repeated elements. A 