
def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest second value.
    """
    return sorted(lst)[-1][1]

# Test your function
print(f([(1, 2), (3, 4)]))
</cell>
<text>
Exercise 3
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given [1, 1, 2, 3, 4, 4, 4, 4] it should return [1, 2, 3, 4].

Hint: You can use the function set() to remove duplicates.


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list with all of the duplicates removed.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
# Test your function
print(remove_duplicates([1, 1, 2, 3, 4, 4, 4, 4]))
</cell>
<text>
Exercise 4
Write a function that returns a list of numbers that sum to zero, using the formula $ \sum_{i=1}^{n} i$ where $n$ is the length of the list.

For example, sum([1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]) should return $16$.

Hint: You can use the sum() built-in function and the len() built-in function to make this problem easier.


</text>
<cell>
def sum_of_list(lst):
    """
    Given a list of numbers, return a list that sums to zero.
    """
    
    # Your code here
    
    return sum(lst)
</cell>
<cell>
# Test your function
print(sum_of_list([1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]))
</cell>
<text>
Exercise 5
Write a function that returns a list of numbers that sums to zero, using the formula $ \sum_{i=1}^{n} i$ where $n$ is the length of the list.

For example, sum([1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]) should return $16$.

Hint: You can use the sum() built-in function and the len() built-in function to make this problem easier.


</text>
<cell>
def sum_of_list(lst):
    """
    Given a list of numbers, return a list that sums to zero.
    """
    
    # Your code here
    
    return sum(lst)
</cell>
<cell>
# Test your function
print(sum_of_list([1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]))
</cell>
<text>
Exercise 6
Write a function that returns a list of numbers that sums to zero, using the formula $ \sum_{i=1}^{n} i$ where $n$ is the length of the list.

For example, sum([1, 2, 3 ,4 ,5 ,6 