
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 5, 3 or 2, we get 2, 3, 4, 5, 6, 8 and 9. The product of these multiples is 51840.
    Return the product of all the multiples of 5, 3 or 2 below 197.
    """    
    
    multiples = []
    
    for n in range(2, int(math.sqrt(197)) + 1):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            multiples.append(n)
            
    return multiples[len(multiples) - 1]
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

where $F_n$ is the n-th number in the Fibonacci sequence. For example, the 6th number in the sequence is $F_5 = 5$. The first two terms of the Fibonacci sequence are $F_1$ and $F_2$, so the first 10 terms are $F_1$, $F_2$, ... $F_10$, then $F_11$ and so on. By convention, $0$ is used to indicate the first term of the sequence.

By starting with $F_0$ and $F_1$, we can compute the sequence $F_2$ to $F_9$ as follows:

$F_2 = F1 + F_0$
$F_3 = F_2 + F_1$
$F_4 = F_3 + F_2$
...
$F_9 = F_8 + F_7$

Notice that $F_n = F{n-1} + F_{n-2}$. So we can compute the entire sequence $F_2$ to $F_9$ by extending the above definition:

$F_2 = F1 + F_0$
$F_3 = F_2 + F_1$
$F_4 = F_3 + F_2$
...
$F_9 = F_8 + F_7$
$F_2 = F_3 + F_4$
$F_3 = F_4 + F_5$
$F_4 = F_5 + F_6$
...
$F_9 = F_8 + F_7$
$F_2 = F_5 + F_6$
$F_3 = F_6 + F_7$
$F_4 = F_7 + F_8$
...
$F_9 = F_8 + F_7$

By computing the above formula for $F_i$, we can generate the entire sequence. For example, starting with $F_0$ and $F_1$, we can generate the $F_2$ to $F_9$ sequence by extending the above definition:

$F_2 = F1 + F_0$
$F_3 = F_2 + F_1$
$F_4 = F_3 + F_2$