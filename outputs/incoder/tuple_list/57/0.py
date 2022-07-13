
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    return max(lst, key=lambda x: x[-1])


# Test your function
print(some_func([(7, 0, 9), (6, 5, 8), (4, 3, 2)]))
</cell>
<text>
Expected output
[(2, 5, 8)]

</text>
<text>
Write a function that takes in a list of numbers and returns the number of even values.

You may find the find the count function useful.


</text>
<cell>
def count_evens(lst):
    """
    Count the number of even numbers in a list of numbers.
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


# Test your function
print(count_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
</cell>
<text>
Expected output
5

</text>
<text>
Write a function that takes in a list of numbers and returns their sum.

This first function should check if the input list is empty. If it is empty, return 0
If the input list has one number, return that number
If the input list has two numbers, return their sum


</text>
<cell>
def sum_of_nums(lst):
    """
    Sum the numbers in a list
    """
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return sum(lst)


# Test your function
print(sum_of_nums([]))
print(sum_of_nums([1, 2, 3]))
print(sum_of_nums([1, 2, 3, 4]))
print(sum_of_nums([1, 2, 3, 4, 5]))
</cell>
<text>
Expected output
0
6
15
15

</text>
<text>
Write a function that takes in a list of numbers and returns their average.

This first function should check if the input list is empty. If it is empty, return 0
If the input list has one number, return that number
If the input list has two numbers, return the average of the two numbers


</text>
<cell>
def avg_of_nums(lst):
    """
    Calculate the average of the numbers in a list
    """
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return sum(lst) / len(lst)


# Test your function
print(avg_of_nums([]))
print(avg_of_nums([1, 2, 3]))
print(avg_of_nums([1, 2, 3, 4]))
print(avg_of_nums([1, 2, 3, 4, 5]))
</cell>
<text>
Expected output
0
2.5
3.5
4.666666666666667

</text>
<text>
Write a Python function that returns a list of numbers, such that duplicates are removed from the list. Your function should return a sorted copy of the list.


</text>
<cell>
def remove_duplicates(lst):
    """
    