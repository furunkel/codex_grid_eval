
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest eleventh value.
    """
    
    lst = sorted(lst)
    
    return lst[2][11]

# Test your function
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(f(lst))
</cell>
<text>
Write a function that returns the sum of the numbers in a list. Except the number 0, you don't need to check if it's in the list.


</text>
<cell>
def f(x):
    """
    sum the numbers in a list
    """
    
    return sum(x)
    
# Test your function
print(f([2, 3, 5, 7, 11]))
</cell>
<text>
Write a function that returns a list of numbers, such that nums[0] + nums[1] = nums[2] + nums[3]. Except that your function should work for any size list of numbers.


</text>
<cell>
def f(x):
    """
    returns a list of numbers, such that nums[0] + nums[1] = nums[2] + nums[3]
    """
    
    return [x[0] + x[1], x[2] + x[3]]
    
# Test your function
print(f([2, 3, 5, 7, 11]))
</cell>
<text>
Write a function that checks whether a number is in a given range (Inclusive of high and low)


</text>
<cell>
def f(x, low, high):
    """
    checks whether a number is in a given range (Inclusive of high and low)
    """
    
    return low <= x <= high
    
# Test your function
print(f(2, 3, 4))
</cell>
<text>
Write a function that checks whether a number is in a given range (Exclusive of high and low)


</text>
<cell>
def f(x, low, high):
    """
    checks whether a number is in a given range (Exclusive of high and low)
    """
    
    return low < x <= high
    
# Test your function
print(f(2, 3, 4))
</cell>
<text>
Write a function that checks whether a number is in a given range (Both high and low limit)


</text>
<cell>
def f(x, low, high):
    """
    checks whether a number is in a given range (Both high and low limit)
    """
    
    return low <= x <= high
    
# Test your function
print(f(2, 3, 4))
</cell>
<text>
Write a function that checks whether a number is in a given range (High limit only)


</text>
<cell>
def f(x, low, high):
    """
    checks whether a number is in a given range (High limit only)
    """
    
    return low <= x
    
