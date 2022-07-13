
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2 or 5, we get 2 and 4. The sum of these multiples is 6.
    Return the sum of all the multiples of 2 or 5 below 500.
    """    
    sum = 0
    for i in range(500):
        if i % 5 == 0:
            sum += i
        elif i % 2 == 0:
            sum += i
    return sum

#print(multiples())
</cell>
<text>
Problem 8
Let's write code that loops through all the numbers of the Fibonacci sequence and checks to see if the sum of the numbers is 10.

The Fibonacci sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

What is the first number that comes after the 30th Fibonacci number?

</text>
<cell>
def fibonacci():
    """
    We want to find the first number in the Fibonacci sequence that comes after the 30th Fibonacci number. 
    We start at 0 and 1, and add them together until we get to the 30th Fibonacci number. 
    We then add that number to the sum.
    """
    sum = 0
    fib1 = 1
    fib2 = 1
    for i in range(30):
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
    return sum

#print(fibonacci())
</cell>
<text>
Problem 9
Write a function that takes in a positive parameter n and returns the nth number of the Fibonacci sequence. 
For example fibonacci(3) = 1.


</text>
<cell>
def fibonacci(n):
    """
    We want to find the nth number in the Fibonacci sequence that comes after the 30th Fibonacci number. 
    We start at 0 and 1, and add them together until we get to the nth Fibonacci number. 
    We then add that number to the sum.
    """
    sum = 0
    fib1 = 1
    fib2 = 1
    for i in range(n):
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
    return sum

#print(fibonacci(3))
</cell>
<text>
Problem 10
Write a function that takes in a positive parameter n and returns the nth number of the Fibonacci sequence. 
For example fibonacci(3) = 1.


</text>
<cell>
def fibonacci(n):
    """
    We want to find the nth number in the Fibonacci sequence that comes after the 30th Fibonacci number. 
    We start at 0 and 1, and add them together until we get to the nth Fibonacci number. 
    We then add 