
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 5, 3 or 2, we get 2, 3 and 4. The sum of these multiples is 9.
    Return the sum of all the multiples of 5, 3 or 2 below 500.
    """    
    sum = 0
    for n in range(500):
        if n % 5 == 0 or n % 3 == 0 or n % 2 == 0:
            sum += n
    return sum

print(multiples())
</cell>
<text>
Great! Now you know how to check if a number is even or odd, and how to sum all the multiples of 3 or 5 below a certain number. Still, it's nice to know how to generate all the multiples of 3 or 5 below a certain number.

The function below is called fibonacci. It takes in a number $n$ and returns the sum of all the multiples of 3 or 5 below $n$.


</text>
<cell>
def fibonacci(n):
    """
    Takes in a number $n$ and returns the sum of all the multiples of 3 or 5 below $n$.
    """
    sum = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        sum += b
    return sum

print(fibonacci(10))
</cell>
<text>
If you want an infinite number of fibonacci numbers, you can use the while True loop as follows:


</text>
<cell>
def fibonacci(n):
    """
    Takes in a number $n$ and returns the sum of all the multiples of 3 or 5 below $n$.
    """
    sum = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        sum += b
    return sum

print(fibonacci(10))
</cell>
<text>
Exercise
Write a function that takes in a list of numbers and returns the sum of the numbers in the list. For example, sum([1, 2, 3]) should return 6. Make sure you use recursion to solve this problem. Hint: You can use a for loop to iterate through the list.


</text>
<cell>
def sum_list(lst):
    """
    Takes in a list `lst` and returns the sum of the numbers in the list.
    """
    sum = 0
    for n in lst:
        sum += n
    return sum

print(sum_list([1,2,3]))
</cell>
<text>
Exercise
Write a function that takes in a list of numbers and returns the product of the numbers in the list. For example, product([2, 3, 4]) should return 24. Make sure you use recursion to solve this problem. Hint: You can use a for loop to iterate through the list.


</text>
<cell>
def product_list(lst):
    """
    Takes in a list `lst` and returns the product of the numbers in the list.
    """
    product = 1
    for n in lst:
        product *= n
    return product

print(product_list([2, 3, 4]))
</cell>
<text>
Exerci