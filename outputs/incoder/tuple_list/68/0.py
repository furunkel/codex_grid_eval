
def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    return max(lst, key=lambda t: t[-1])

# Test your function
print(f([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (1, 5), (2, 6)]))
</cell>
<text>
The lambda function can take in multiple arguments, and it can return a value that depends on multiple arguments. For example:


</text>
<cell>
def f(a, b, c):
    return a + b + c

print(f(1, 2, 3))
</cell>
<text>
Write a function that accepts a string and returns the number of uppercase letters in that string.

Hint: Use a for loop!


</text>
<cell>
def count_upper(s):
    """
    Count the number of uppercase letters in a string.
    """
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count

# Test your function
print(count_upper("How are you? I am fine, thanks"))
</cell>
<text>
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $0\leq i\leq n$. Test your function on $n=10$.


</text>
<cell>
def squares(n):
    """
    Return a list of squares of integers from 0 to n
    """
    return [i ** 2 for i in range(n)]

# Test your function
print(squares(10))
</cell>
<text>
Write a function that returns a list of cubed numbers, such that $x^3=x^4$, for all $0\leq i\leq n$. Test your function on $n=10$.


</text>
<cell>
def cubes(n):
    """
    Return a list of cubes of integers from 0 to n
    """
    return [i ** 3 for i in range(n)]

# Test your function
print(cubes(10))
</cell>
<text>
Write a function that returns the sum of the squares of the first n numbers. Your function should work for any value of $n$, including 0.


</text>
<cell>
def sum_squares_first_n(n):
    """
    Return the sum of the squares of the first n numbers
    """
    return sum([i ** 2 for i in range(n)])

# Test your function
print(sum_squares_first_n(10))
</cell>
<text>
Write a function that accepts a string and returns a list of all the characters in that string. Your function must work for any value of $n$, including 0.


</text>
<cell>
def all_chars(s):
    """
    Return a list of all characters in s
    """
    return list(s)

# Test your function
print(all_chars("How are you? I am fine