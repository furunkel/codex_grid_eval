
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[-1])
</cell>
<cell>
# Test your code
lst = [('Bob', 40), ('Alex', 50), ('Adam', 60), ('John', 70)]
print(tuple_extract(lst))
</cell>
<text>
Expected output
('Bob', 40)

</text>
<text>
Question 7
Create a function that returns a list of numbers, such that $x_i=i^2$, for all $0\leq i \leq 9$.

The function should return a list of length 10, and all numbers in the list should be integers.

Hint: You can use a for-loop!


</text>
<cell>
def squares(max_num):
    """
    Generate a list of squares from 0 to max_num.
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    # Your code here
    
    return [i ** 2 for i in range(max_num)]
</cell>
<cell>
# Test your code
print(squares(10))
</cell>
<text>
Expected output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

</text>
<text>
Question 8
Create a function that returns a list of numbers, such that $x_i=i^3$, for all $0\leq i \leq 9$.

The function should return a list of length 10, and all numbers in the list should be integers.

Hint: You can use a for-loop!


</text>
<cell>
def cubes(max_num):
    """
    Generate a list of cubes from 0 to max_num.
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    # Your code here
    
    return [i ** 3 for i in range(max_num)]
</cell>
<cell>
# Test your code
print(cubes(10))
</cell>
<text>
Expected output
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

</text>
<text>
Question 9
Create a function that returns a list of numbers, such that $x_i=i^4$, for all $0\leq i \leq 9$.

The function should return a list of length 10, and all numbers in the list should be integers.

Hint: You can use a for-loop!


</text>
<cell>
def fibonacci(max_num):
    """
    Generate a list of fibonacci numbers from 0 to max_num.
    
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    
    # Your code here
    
    return [i ** 4 for i in range(max_num)]
</cell>
<