
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2 or 5, we get 2, 4, 5, 6, 8, 10, 12 and 14. The sum of these multiples is 61.
    Return the sum of all the multiples of 2 or 5 below 200.
    """    
    
    sum = 0
    for i in range(1, 200):
        if i % 2 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

print(multiples())
</cell>
<text>
Great! Now you know how to sum all the multiples of 2 and 5 below 200.

Problem 3: Recursion
Let's see an example of where recursion can be used.


</text>
<cell>
def factorial(n):
    """
    Recursive factorial function
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
</cell>
<text>
In this example, we've used the factorial function above to calculate the factorial of 5, but how would you extend this to calculate the factorial of any number?

You could calculate the factorial of any number by using the following steps:

Calculate factorial(5) - how would you do this?
Multiply this by 5 - how would you do this?
Repeat steps 1 and 2 until you reach a number less than or equal to 1 (or 0).

In this way, you could calculate the factorial of any number, not just 5.

Problem 4: Fibonacci
The fibonacci sequence is defined by the recurrence relation:

$Fn = F{n-1} + F_{n-2}$

where $F_0 = 0$ and $F_1 = 1$. For example, as 1, 3, 6, 10, etc.

Using the above relation:

$Fn = F{n-1} + F_{n-2} = F{n-1}(0) + 2F_{n-2}(1) = F{n-1}(0) + F_{n-2}(1) = 2F_0 + 2F_1$

Using the formula for the sum of two numbers, we get:

$Fn = F{n-1} + F_{n-2} = F{n-1}(0) + 2F_{n-2}(1) + F{n-1}(0) + 2F_{n-2}(2) = F{n-1}(0) + 2F_{n-2}(1) + (0 + 2F_0) + 2F_1(1) = F{n-1}(0) + 2F_{n-2}(1) + (0 + 2F_0) + 2F_1(2) = F{n-1}(0) + 2F_{n-2}(1) + (0 + 2F_0) + 2F_1(3) + 2F_2(2) = F{n-1}(0) + 2F_{n-2}(1) + (0 + 2F_0) + 2F_1(3) + 2F_2(3) + F{n-1}(0) + 2F_{n-2}(2) = F{n-1}(0) + 2