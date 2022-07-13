
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    
    smallest = lst[0]
    largest = lst[0]
    
    for x in lst:
        if x[0] == smallest[0]:
            smallest = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10])
        elif x[0] == largest[0]:
            largest = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10])
    
    return smallest
</cell>
<cell>
min_max([(1,2,3,4,5,6,7,8,9,10),(11,12,13,14,15,16,17,18,19,20),(21,22,23,24,25,26,27,28,29,30),(31,32,33,34,35,36,37,38,39,40),(41,42,43,44,45,46,47,48,49,50),(51,52,53,54,55,56,57,58,59,60),(61,62,63,64,65,66,67,68,69,70),(71,72,73,74,75,76,77,78,79,80),(81,82,83,84,85,86,87,88,89,90),(91,92,93,94,95,96,97,98,99,100)])
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns the sum of the elements of the list.


</text>
<cell>
def sum(lst):
    """
    Given a list of numbers, return the sum of the numbers in the list.
    """
    
    sum = 0
    
    for x in lst:
        sum += x
    
    return sum
</cell>
<cell>
sum([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns the product of the elements of the list.


</text>
<cell>
def product(lst):
    """
    Given a list of numbers, return the product of the numbers in the list.
    """
    
    product = 1
    
    for x in lst:
        product *= x
    
    return product
</cell>
<cell>
product([1,2,3,4,5,6,7,8,9,10])
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns the sum of the squares of the elements of the list.


</text>
<cell>
def sum_squared(lst):
    """
