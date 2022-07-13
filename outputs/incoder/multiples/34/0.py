
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 5, we get 2, 4, 5, 6 and 8. The sum of these multiples is 25.
    Return the sum of all the multiples of 2 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 201):
        if i % 2 == 0 or i % 5 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 3
The Fibonacci sequence is defined by the recurrence relation:

$Fn = F{n-1} + F_{n-2}$

where $F_0 = 0$ and $F_1 = 1$. By starting with $F_0 = 0$ and $F_1 = 1$ and continuing 
to $F_n = F{n-1} + F_{n-2}$ and $F_{n}$ remains unchanged, we get the following sequence:

$F{n} = \left( F_{n-1} + F_{n-2}\right)$

Using the rule above and starting with $F_0 = 0$ and $F_1 = 1$, we can compute $F_2$ and $F_3$ as follows:

$F_2 = F1 + F2$
$F_3 = F2 + F_3$

When $F_n = F_{n-1} + F_{n-2}$, where $n$ is greater than 1, the values of $F_n$ are repeatedly computed until $F_n$ equals $F{n-1} + F_{n-2}$.

By iterating this process, we get the following sequence:

$Fn = F{n-1} + F_{n-2} + \cdots + F_2$

$F_n = \left( F_{n-1} + F_{n-2}\right) + \cdots + F_2$

$F_n = \left( F_{n-1} + F_{n-2}\right) + \cdots + F_2 + \cdots + F_1$

$F_n = \left( F_{n-1} + F_{n-2}\right) + \cdots + F_2 + \cdots + F_1 + \cdots + F_0$

Using the formula $Fn = F{n-1} + F_{n-2} + \cdots + F_2$ and starting with $F_0 = 0$ and $F_1 = 1$, 
we get:

$Fn = F{n-1} + F_{n-2} + \cdots + F_2 + F_1$

$F_n = \left( F_{n-1} + F_{n-2}\right) + \cdots + F_2 + F_1$

$F_n = \left( F_{n-1} + F_{n