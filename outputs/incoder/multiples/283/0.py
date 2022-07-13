
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 5, 3 or 2 below 124.
    """    
    
    multiples = []
    
    for n in range(124, 1, -1):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            multiples.append(n)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the formula:

$Fn = \begin{cases}
1 & n = 0\
1 & n = 1 \
F{n-1} + F_{n-2} & n > 1
\end{cases}$

where $F_n$ is the n-th number in the Fibonacci sequence. For example, the 6th number in the sequence is $F_5 = 5$. The first few terms of the Fibonacci sequence are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229.


</text>
<cell>
def fibonacci():
    """
    Fibonacci numbers are defined by the formula:
    
    $Fn = \begin{cases}
    1 & n = 0\
    1 & n = 1 \
    F{n-1} + F_{n-2} & n > 1
    \end{cases}$
    
    where $F_n$ is the n-th number in the Fibonacci sequence. 
    For example, the 6th number in the sequence is $F_5 = 5$. The first few terms of the Fibonacci sequence are:
    
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229.
    """
    
    fib = [0, 1]
    
    for n in range(2, 12):
        fib.append(fib[-1] + fib[-2])
        
    return fib
</cell>
<cell>
fibonacci()
</cell>
<text>
Problem 4
The itertools module has a number of recipes for generating permutations and combinations very efficiently. One of these recipes is itertools.combinations_with_replacement(), which generates all possible combinations of a given set of objects with replacement.

For example, list(itertools.combinations_with_replacement(range(5), 3)) generates all 5-item combinations of length 3 with replacement