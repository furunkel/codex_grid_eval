
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest last value.
    """
    return max(lst)[1]

# Test your function
print(some_func([(7, 4), (2, 9), (3, 8), (5, 3)]))
</cell>
<text>
Exercise 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the numbers in the list. For example, sum([1, 2, 3]) should return [1, 2, 3].

Hint: You can start your function with def sum_list(lst)


</text>
<cell>
def sum_list(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the numbers in the list.
    """
    
    return lst
</cell>
<cell>
# Test your function
print(sum_list([1,2,3]))
</cell>
<text>
Exercise 4
Write a function that takes a list and returns a new list with all of the elements doubled. For example [1,2,3] should return [2, 4, 6].

Hint: You can start your function with def double_list(lst)


</text>
<cell>
def double_list(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the numbers in the list.
    """
    
    return lst
</cell>
<cell>
# Test your function
print(double_list([1,2,3]))
</cell>
<text>
Exercise 5
Write a function that takes a list and returns a new list with all of the elements multiplied by two. For example [1,2,3] should return [2, 4, 6].

Hint: You can start your function with def double_list(lst)


</text>
<cell>
def double_list(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the numbers in the list.
    """
    
    return lst
</cell>
<cell>
# Test your function
print(double_list([1,2,3]))
</cell>
<text>
Exercise 6
Write a function that checks whether a number is in a given list or not. For example:

my_list = [1,2,3,4,5,6,7,8,9,10]
check_if_in_list(my_list, 3) should return True
check_if_in_list(my_list, 9) should return False

Hint: You can start your function with def in_list(my_list, number)


</text>
<cell>
def in_list(my_list, number):
    """
    Given a list and a number, check if number is in the list or not
    """
    
    return number
</cell>
<cell>
# Test your function
print(in_list([1,2,3,4,5,6,7,8,9,10], 3))
print(in_list([1,2,3,4,5,6,7,8,9,10], 9))
</cell>
<text>
Exercise 7