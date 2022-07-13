
def multiples():
    """
    If we list all the natural numbers below 10 that are multiples of 2 or 9, we get 2, 4, 6, 8 and 9. The sum of these multiples is 29.
    Return the sum of all the multiples of 2 or 9 below 124.
    """    
    
    sum_of_multiples = 0
    
    for i in range(124, 1, -1):
        if i % 2 == 0:
            sum_of_multiples += i
        else:
            sum_of_multiples += 9
            
    return sum_of_multiples
</cell>
<cell>
# Check
print(multiples())
</cell>
<text>
Write a function that returns the product of numbers from 1 to n, where 1 ≤ n ≤ 10.
Example: For n = 10, the output should be
products_of_numbers_between(1,10) = [1,2,3,4,5,6,7,8,9,10]

</text>
<cell>
def products_of_numbers_between(start, end):
    """
    products_of_numbers_between(1,10) = [1,2,3,4,5,6,7,8,9,10]
    """
    
    products = []
    
    for i in range(start, end+1):
        products.append(i)
        
    return products
</cell>
<cell>
# Check
print(products_of_numbers_between(1,10))
</cell>
<text>
Write a Python function that returns True if the number is prime and False otherwise.
A number is prime if that number is only divisible by 1 and itself.
Example: For num = 6, the output should be
is_prime(6) = True.

</text>
<cell>
def is_prime(num):
    """
    Checks to see if a number is prime.
    """
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True
</cell>
<cell>
# Check
print(is_prime(6))
</cell>
<text>
Write a Python function that returns the sum of the numbers from 1 to n that are divisible by k.
Example: For n = 10 and k = 2, the output should be
sum_of_multiples_below_n(10, 2) = 22
Hint: 2 ≤ k ≤ n ≤ 50

</text>
<cell>
def sum_of_multiples_below_n(num, k):
    """
    Sum of multiples of numbers below n that are divisible by k.
    """
    
    sum_of_multiples = 0
    
    for i in range(1, num+1):
        if i % k == 0:
            sum_of_multiples += i
            
    return sum_of_multiples
</cell>
<cell>
# Check
print(sum_of_multiples_below_n(10, 2))
</cell>
<text>
Write a Python function that returns the product of the numbers from 1 to n that are divisible by k.
Example: For n = 10 and k = 2, the output should be
product_of_multiples_below_n(10, 2) = 600
Hint: 2 ≤ 