
def generate_dict(n):
    """
    With a given integral number n, write a program to generate a dictionary that contains (i, i - i) such that
    i is a integral number between 1 and n (both included) and then the program should return the dictionary.
    
    Suppose the following input is supplied to the function:
    8
    Then, the output should be:
    {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    """
    
    dict = {}
    
    for i in range(1, n + 1):
        
        if i not in dict:
            dict[i] = i - i
            
    return dict
</cell>
<cell>
# Test your code
assert generate_dict(8) == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, "Your code should return {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}."
</cell>
<text>
The Fibonacci Sequence
The Fibonacci sequence is defined by the following relation:

$Fn = \begin{cases}
1 & n = 1 \
1 & n = 2 \
F{n-1} + F_{n-2} & n > 2
\end{cases}$

where $F_n$ is the n-th number in the Fibonacci sequence. An example of a non-trivial Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

The Fibonacci sequence is commonly used in mathematics and computer science to describe the running total of some event; for example, the sum of the first $n$ natural numbers is called the $n$-th Fibonacci number, since the first two numbers are $1$ and $2$.

The first few terms of the sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

By starting with $1$ and $2$, one can iteratively compute the next $n$ terms of the sequence. For example, the 6th term of the sequence is $1 + 2 = 3$, and the 8th term is $3 + 5 = 8$, and so on. The $n$-th term therefore becomes:

$Fn = F{n-1} + F_{n-2}$

Using the formula $Fn = F{n-1} + F_{n-2}$ and assuming $F_0 = 1$ and $F_1 = 1$, one gets the following Python code to print the $n$-th term of the Fibonacci sequence:


</text>
<cell>
def fibonacci(n):
    """
    Compute the $n$-th term of the Fibonacci sequence
    
    INPUT:
    
    n - an integer
    
    OUTPUT:
    
    the $n$-th term of the Fibonacci sequence
    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 