
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    
    return max(lst, key=lambda x:x[1])

#test
print(min_max([(4,2), (5,3), (6,4), (7,5), (8,6), (9,7), (10,8), (11,9), (12,10)]))
</cell>
<text>
Problem 7
Write a function that returns the sum of the numbers in a list. For example, sum([1, 2, 3]) should return 6.

HINT: You can use the sum function with a generator expression


</text>
<cell>
def sum_list(lst):
    """
    Given a list of numbers, return the sum of those numbers.
    """
    
    return sum(lst)
    
#test
print(sum_list([1,2,3]))
</cell>
<text>
Problem 8
Write a function that takes a list and returns a new list with only the even numbers in it. For example, given a list [1,2,3,4,5,6,7,8,9], your function should return [2,4,6,8].

HINT: You can use the filter function with a lambda expression


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the even numbers in it.
    """
    
    return list(filter(lambda x:x%2==0, lst))

#test
print(even_numbers([1,2,3,4,5,6,7,8,9]))
</cell>
<text>
Problem 9
Write a function that takes a list and returns a new list with only the odd numbers in it. For example, given a list [1,2,3,4,5,6,7,8,9], your function should return [1,3,5,7,9].

HINT: You can use the filter function with a lambda expression


</text>
<cell>
def odd_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the odd numbers in it.
    """
    
    return list(filter(lambda x:x%2!=0, lst))

#test
print(odd_numbers([1,2,3,4,5,6,7,8,9]))
</cell>
<text>
Problem 10
Write a function that takes a list and returns a new list with all the numbers that are not evenly divisible by 7. For example, given a list [1,2,3,4,5,6,7,8,9], your function should return [1,2,4,5,6,8,9].

HINT: You can use the filter function with a lambda expression


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of numbers, return a new list containing only the even numbers in it.
    """
    
    return list(filter(lambda x:x%2!=0 and x%7!=0, lst))

#test
print(even_numbers([1,2,3,4,5,6,7,8,9]))
</cell>
<text>
Problem 11
Write a function that 