
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The product of these multiples is 8.
    Return the product of all the multiples of 2 or 5 below 500.
    """    
    
    multiples = []
    
    for i in range(500):
        if i % 2 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to find the sum of all the multiples of 2 or 5 below a certain number. Can you find the sum of all the multiples of 2 below a certain number?


</text>
<cell>
def sumOfMultiples2(n):
    """
    Sum of all the multiples of 2 below n
    """
    
    multiples = []
    
    for i in range(n):
        if i % 2 == 0:
            multiples.append(i)
    
    return sum(multiples)
</cell>
<cell>
sumOfMultiples2(10)
</cell>
<text>
Perfect! You are done.

</text>
<text>
Problem 7 - Tribonacci numbers
The sum of the first ten tribonacci numbers is given below. Find the sum of all the numbers in the Fibonacci sequence whose first 10 terms are 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...


</text>
<cell>
def sumOfTribonacci(n):
    """
    Sum of first 10 tribonacci numbers
    """
    
    sum = 0
    
    for i in range(10):
        sum += i
        
    return sum
</cell>
<cell>
sumOfTribonacci(10)
</cell>
<text>
Problem 8 - Factorial
A factorial is a number multiplied by all the numbers from 1 to it. So the 7! = 7 x 6 x 5 = 42 x 10 = 9 + 4 x 3 = 73.

The first few factorials are:

1! = 1
2! = 2 
3! = 6 
4! = 24
5! = 120 
6! = 720 
7! = 5040 
8! = 362880 
9! = 39916800 
10! = 403206400 
11! = 40320640 
12! = 362880640 
13! = 399168064 
14! = 362880640 
15! = 399168064 
16! = 362880640 
17! = 399168064 
18! = 362880640 
19! = 399168064 
20! = 362880640 
21! = 399168064 
22! = 362880640 
23! = 3991680