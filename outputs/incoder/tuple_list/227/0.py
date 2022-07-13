
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    
    return max(lst)[1]

# Test Cases
print(min_max([(3,4), (5,6), (7,8)]))
print(min_max([(3,4), (5,6), (7,8), (9,10)]))
print(min_max([(3,4), (5,6), (7,8), (9,10), (11,12)]))
print(min_max([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14)]))
</cell>
<text>
Problem 7
Write a function that returns the sum of the numbers in a list. For example, sum([1, 2, 3]) should return 6.


</text>
<cell>
def sum_list(lst):
    """
    Given a list of numbers, return the sum of those numbers.
    """
    
    return sum(lst)

# Test Cases
print(sum_list([1,2,3]))
print(sum_list([1,2,3,4,5]))
</cell>
<text>
Problem 8
Write a function that returns a list consisting of the first n prime numbers. For example, primes(10) should return [2, 3, 5, 7, 11, 13, 17, 19]


</text>
<cell>
def primes(n):
    """
    Given a number n, return a list of all prime numbers less than or equal to n.
    """
    
    lst = []
    
    for i in range(2, n):
        if isprime(i):
            lst.append(i)
            
    return lst

def isprime(n):
    """
    Given a number n, return True if n is a prime number and False otherwise.
    """
    
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Test Cases
print(primes(10))
print(primes(100))
</cell>
<text>
Problem 9
Write a function that returns a list of all the even numbers in a given list. For example, evens([1, 3, 5]) should return [2, 4]. Make sure your function works with any list including an empty list.


</text>
<cell>
def evens(lst):
    """
    Given a list of numbers, return a list of all even numbers in the list.
    """
    
    lst2 = []
    
    for i in lst:
        if i % 2 == 0:
            lst2.append(i)
            
    return lst2

# Test Cases
print(evens([1, 3, 5]))
print(evens([]))
</cell>
<text>
Problem 10
Write a function that returns a list of all the numbers from 1 to n that are divisible by all numbers from 1 to m. For example, divisible(10, 5) should return [5, 7, 9, 11]. Make sure your function works with any n and m.


</text>
<cell>
def divisible(n, m):
    """