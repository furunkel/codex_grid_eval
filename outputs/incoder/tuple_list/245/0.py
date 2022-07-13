
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest third value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][2]
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list. For example, square([1,2,3]) should return [1,4,9], square([4,5,6]) should return [16,25,36] and so on.


</text>
<cell>
def square(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers in the original list.
    """
    
    lst2 = []
    
    for i in lst:
        lst2.append(i**2)
    
    return lst2
</cell>
<cell>
square([1,2,3])
</cell>
<cell>
square([4,5,6])
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list divided by the sum of the squares of the elements in the original list. For example, square_divide([1,2,3]) should return [1,4,9] square_divide([4,5,6]) should return [16,25,36] and so on.


</text>
<cell>
def square_divide(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers in the original list divided by the sum of the squares of the numbers in the original list.
    """
    
    lst2 = []
    
    for i in lst:
        lst2.append(i**2)
        lst2.append(i**0.5)
    
    return lst2
</cell>
<cell>
square_divide([1,2,3])
</cell>
<cell>
square_divide([4,5,6])
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the elements in the original list divided by the sum of the squares of the elements in the original list squared plus one. For example, square_plus_one([1,2,3]) should return [1,4,9] square_plus_one([4,5,6]) should return [16,25,36] and so on.


</text>
<cell>
def square_plus_one(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers in the original list divided by the sum of the squares of the numbers in the original list squared plus one.
    """
    
    lst2 = []
    
