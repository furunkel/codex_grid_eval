
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0 or i % 9 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Write a function that computes the factorial of a number. Do not use the multiplication operator (*) but instead use the fact that $n! = n \times n-1 \times n-2 \times ...1$

Example

$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$

$4! = 4 \times 3 \times 2 \times 1 = 24$

$3! = 3 \times 2 \times 1 = 6$

$2! = 2 \times 1 = 1$


</text>
<cell>
def factorial(n):
    """
    Compute the factorial of a number
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
</cell>
<cell>
factorial(5)
</cell>
<text>
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Example

'Hello World'
'HaB1c3d4e5F6g7H8'
'This sentence is going to make you cry.'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na d67 f56 g78'
'ra5na 