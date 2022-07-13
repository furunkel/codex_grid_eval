
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 2, 3 or 5, we get 2, 3, 4, 5, 6, 8, 9, 10, 12 and 14. The sum of these multiples is 73.
    Return the sum of all the multiples of 2, 3 or 5 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 2 == 0:
            sum += i
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
    return sum
</cell>
<cell>
multiples()
</cell>
<text>
Problem 8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


</text>
<cell>
def prime_numbers():
    """
    List the first six prime numbers: 2, 3, 5, 7, 11, and 13.
    """
    
    primes = []
    
    for i in range(2, 100001):
        if isprime(i):
            primes.append(i)
    return primes
</cell>
<cell>
prime_numbers()
</cell>
<text>
Problem 9
Write a function that returns the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

Example 1:

Input: [1,5,1,5,6,7,8,6]
Output: 10
Explanation: The sum of all the numbers in the array is 3 + 5 + 8 + 0 + 6 = 17.

Example 2:

Input: [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Output: 42
Explanation: The sum of all the numbers in the array is 3 + 5 + 7 + 9 + 14 = 54.


</text>
<cell>
def sum_of_array_except_for_6s_and_7s(arr):
    """
    Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7).
    
    arr: a list of integers
    return: the sum of the numbers in the array
    """
    
    sum = 0
    
    for i in range(len(arr)):
        if arr[i] != 6:
            sum += arr[i]
        elif arr[i] == 6:
            sum += arr[i+1]
            
    return sum
</cell>
<cell>
sum_of_array_except_for_6s_and_7s([1,5,1,5,6,7,8,6])
</cell>
<cell>
sum_of_array_except_for_6s_and_7s([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
</cell>
<text>
Problem 10
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

731671765313306249192251196744