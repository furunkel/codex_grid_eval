
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest last value.
    """
    
    # Your code here
    
    return max(lst)[1]

# Test your function
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)]
print(f(lst))
</cell>
<text>
Great job!

</text>
<text>
Exercise 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first elements in the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the first elements in the list.
    """
    
    # Your code here
    
    return [i**2 for i in lst]

# Test your function
lst = [1, 2, 3, 4, 5]
print(f(lst))
</cell>
<text>
Great job!

</text>
<text>
Exercise 4
Write a function that takes a list and returns a list where each element is the product of the numbers in the list. For example, f(lst) should return [120, 60, 120, 240, 120] because 120 is $2 \times 3$, 60 is $3 \times 4$, 240 is  $4 \times 5$ and $2 \times 4$ is $1 \times 6$.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element is the product of the numbers in the list.
    """
    
    # Your code here
    
    return [i*i for i in lst]

# Test your function
lst = [1, 2, 3, 4, 5]
print(f(lst))
</cell>
<text>
Great job!

</text>
<text>
Exercise 5
Write a function that returns a list containing the first n prime numbers. Test it on [2, 3, 5, 7, 11, 13] and see what happens if you set n = 4.


</text>
<cell>
def f(n):
    """
    Given a number, returns a list of the first n prime numbers.
    """
    
    # Your code here
    
    return [i*i for i in range(3, n+1, 2) if i%2==0]

# Test your function
print(primes(4))
</cell>
<text>
Great job!

</text>
<text>
Exercise 6
Write a function that returns a list of all the prime factors of an integer. Test it on 7 and see if your function works.


</text>
<cell>
def prime_factors(n):
    """
    Given a number, returns a list of the prime factors of that number.
    """
    
    # Your code here
    
    return [i*i for i in range(3, n+1, 2) if i