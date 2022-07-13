
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x:x[0])[2]

# Test your function
print(f([(4,5), (3,2), (1,1)]))
</cell>
<text>
Great Job!

</text>
<text>


</text>
<text>


</text>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. Make sure it handles the case where $n<1$ by raising a ValueError.


</text>
<cell>
def squares(n):
    """
    Write a function that returns a list of numbers, such that x_i=i^2, for 1<=i<=n.
    Your function should raise a ValueError if n<1.
    """
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    
    # Your code here
    return [i**2 for i in range(1, n+1)]
</cell>
<text>
Now write a function that computes the factorial of a number. Your function should call the squares() function to compute the values for $n$, which is 1,2,3,...$n-1$,. Then it should multiply all the values, and finally it should return the factorial of the final result:


</text>
<cell>
def factorial(n):
    """
    Write a function that computes the factorial of a number. The function should 
    call the squares() function to compute the values for $n$, which is 1,2,3,...$n-1$,
    and then it should multiply all the values, and finally it should return the factorial of the final result.
    """
    # Your code here
    return n*factorial(n-1)
</cell>
<text>
Let's see if it works:


</text>
<cell>
print(factorial(4))
print(factorial(5))
print(factorial(6))
</cell>
<text>
And now let's test your function:


</text>
<cell>
print(squares(5))
print(squares(10))
print(squares(15))
print(squares(20))
print(squares(25))
</cell>
<cell>
print(factorial(5))
print(factorial(10))
print(factorial(15))
print(factorial(20))
print(factorial(25))
</cell>
<text>
That looks right!


</text>
<text>
You'll notice that when we get to the end of the list of numbers, the factorial of $n$ is still being computed, so that's why we use the result of the recursive call that stops when $n$ is less than or equal to one.

If you write a function that calls itself (recursion), make sure your base case (when $n=1$) is a call to return (without an argument), or you will 