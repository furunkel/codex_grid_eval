
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz(50)
    3
    """
    if n%3 == 0:
        if n%7 == 0:
            return 1
        else:
            return 0
    elif n%11 == 0:
        return 1
    else:
        return 0
</cell>
<cell>
# Test your code
fizz_buzz(50)
</cell>
<text>
FizzBuzz
Write a program to find the number of 'Fizz' in the number 100. You may assume that the number will contain at least 3 digits. If the number contains 3 or more digits, return 'FizzBuzz'. If it does not, then simply return the number.


</text>
<cell>
def fizz_buzz(n):
    """Return the number of 'Fizz' in the number 100. You may assume that the number will contain at least 3 digits. If the number contains 3 or more digits, return 'FizzBuzz'. If it does not, then simply return the number.
    >>> fizz_buzz(100)
    'FizzBuzz'
    >>> fizz_buzz(101)
    101
    """
    if n%3 == 0:
        if n%7 == 0:
            return 'FizzBuzz'
        else:
            return n
    elif n%11 == 0:
        return 'FizzBuzz'
    else:
        return n
</cell>
<cell>
# Test your code
fizz_buzz(100)
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the formula:

$$ Fn = \begin{cases}
1 & n = 0\
1 & n = 1 \
F{n-1} + F_{n-2} & n > 1
\end{cases}$$

where $F_n$ is the n-th number in the Fibonacci sequence. For example, the 6th number in the sequence is $F_6 = 1$. Implement a function that computes the n-th number in the Fibonacci sequence:


</text>
<cell>
def fibonacci(n):
    """Compute the nth number in the Fibonacci sequence"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
</cell>
<cell>
# Test your code
fibonacci(6)
</cell>
<text>
Problem 4
The Fibonacci sequence is defined by the formula:

$$ Fn = \begin{cases}
1 & n = 0\
1 & n = 1 \
F{n-1} + F_{n-2} & n > 1
\end{cases}$$

