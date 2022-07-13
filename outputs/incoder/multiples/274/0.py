
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 2, 3 or 5 below 500.
    """    
    
    sum = 0
    for i in range(1, 500):
        if i % 2 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Problem 7
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


</text>
<cell>
def primes_below(n):
    """
    Find the sum of all the primes below n.
    """
    
    sum = 0
    for i in range(2, n):
        if i % 2 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        elif i % 7 == 0:
            sum += i
        elif i % 11 == 0:
            sum += i
        elif i % 13 == 0:
            sum += i
        elif i % 17 == 0:
            sum += i
        elif i % 19 == 0:
            sum += i
        elif i % 23 == 0:
            sum += i
        elif i % 29 == 0:
            sum += i
        elif i % 31 == 0:
            sum += i
        elif i % 37 == 0:
            sum += i
        elif i % 41 == 0:
            sum += i
        elif i % 43 == 0:
            sum += i
        elif i % 47 == 0:
            sum += i
        elif i % 53 == 0:
            sum += i
        elif i % 59 == 0:
            sum += i
        elif i % 61 == 0:
            sum += i
        elif i % 67 == 0:
            sum += i
        elif i % 71 == 0:
            sum += i
        elif i % 73 == 0:
            sum += i
        elif i % 79 == 0:
            sum += i
        elif i % 83 == 0:
            sum += i
        elif i % 89 == 0:
            sum += i
        elif i % 97 == 0:
            sum += i
        elif i % 103 == 0:
            sum += i
        elif i % 107 == 0:
            sum += i
        elif i % 113 == 0:
            sum += i
        elif i % 121 == 0:
            sum += i
        elif i % 127 == 0:
            sum += i
        elif i % 131 == 0:
            sum += i
        elif i % 137 == 0:
            sum += i
        elif i % 141 == 0:
            sum += i
        elif i % 147 == 0:
            sum += i
        elif i % 153 == 0:
            sum += i
        elif i % 159 == 0:
            sum += i
        elif i % 161 == 0:
            sum += i
        elif i % 163 == 0:
            sum += i
        elif i % 167 == 0:
            sum += i
        elif i % 173 == 0:
            sum += i
        elif i % 179 == 0:
            sum += i
        elif i % 181 == 0:
            sum += i
        elif i % 191 == 0:
            sum += i
        elif i % 