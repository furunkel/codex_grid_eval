
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    
    lst = sorted(lst)
    
    return lst[2]
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (1, 3), (2, 4)]
print(tuple_extract(lst))
</cell>
<text>
Write a function that returns a list of all the positive integers up to some number N.


</text>
<cell>
def upto(N):
    """
    Returns a list of all the positive integers up to some number N.
    
    >>> upto(10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    lst = []
    
    for i in range(N):
        if i % 2 == 0:
            lst.append(i)
            
    return lst
</cell>
<cell>
# Test your code
print(upto(10))
</cell>
<text>
Write a function that returns a list of all the even numbers from 0 to some number N.


</text>
<cell>
def evens(N):
    """
    Returns a list of all the even numbers from 0 to some number N.
    
    >>> evens(10)
    [0, 2, 4, 6, 8]
    """
    
    lst = []
    
    for i in range(N):
        if i % 2 == 0:
            lst.append(i)
            
    return lst
</cell>
<cell>
# Test your code
print(evens(10))
</cell>
<text>
Write a function that returns a list of all the numbers from 0 to some number N that are divisible by some number M.


</text>
<cell>
def divisbles(N, M):
    """
    Returns a list of all the numbers from 0 to some number N that are divisible by some number M.
    
    >>> divisbles(10, 5)
    [10, 15, 20, 25]
    """
    
    lst = []
    
    for i in range(N):
        if i % M == 0:
            lst.append(i)
            
    return lst
</cell>
<cell>
# Test your code
print(divisbles(10, 5))
</cell>
<text>
Write a function that returns a list of all the numbers from 0 to some number N that are divisible by some number M and also have an even value.


</text>
<cell>
def divisbles_even_n(N, M):
    """
    Returns a list of all the numbers from 0 to some number N that are divisible by some number M and also have an even value.
    
    >>> divisbles_even_n(10, 5)
    [10, 15, 20]
    """
    
    lst = []
    
    for i in range(N):
        if i % M == 0 and i % 2 == 0:
            lst.append(i)
            
    return lst
</cell>
<cell>
# Test 