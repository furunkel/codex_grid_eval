
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 3 or 5, we get  and 3. The sum of these multiples is 3.
    Return the sum of all the multiples of 3 or 5 below 1000.
    """    
    
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

print(multiples())
</cell>
<text>
Problem 7
Write a function that returns the greatest common divisor (GCD) of a and b. GCD is defined to be the largest integer that divides both a and b.


</text>
<cell>
def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of a and b.
    
    GCD is defined to be the largest integer that divides both a and b.
    
    >>> gcd(20, 10)
    10
    >>> gcd(10, 5)
    5
    """
    
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(20, 10))
print(gcd(10, 5))
</cell>
<text>
Problem 8
Write a function that takes two lists of numbers and returns the number of their intersection.


</text>
<cell>
def intersection(list1, list2):
    """
    Calculate the number of their intersection.
    
    >>> intersection([1, 2, 3], [1, 2, 3, 4])
    2
    """
    
    intersection = 0
    
    for i in list1:
        if i in list2:
            intersection = intersection + 1
    
    return intersection

print(intersection([1, 2, 3], [1, 2, 3, 4]))
</cell>
<text>
Problem 9
Write a function that checks whether a passed string is palindrome or not.


</text>
<cell>
def palindrome(s):
    """
    Checks whether the given string is a palindrome or not.
    
    >>> palindrome('racecar')
    True
    >>> palindrome('A man, a plan, a canal: Panama!')
    False
    """
    
    return s == s[::-1]

print(palindrome('racecar'))
print(palindrome('A man, a plan, a canal: Panama!'))
</cell>
<text>
Problem 10
Write a Python function that takes a list and returns a new list with unique elements of the first list.


</text>
<cell>
def unique(list):
    """
    Returns a new list with unique elements of the first list.
    
    >>> unique([1, 1, 2, 3])
    [1, 2, 3]
    """
    
    unique_list = []
    
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

print(unique([1, 1, 2, 3]))
</cell>
<text>
Problem 11
Write a Python function that checks whether a passed string is palindrome or not.


</text>