
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(lst)[2]

# Test your function
print(tuple_extract(lst))
</cell>
<text>
Expected output
4

</text>
<text>
Exercise 4
Write a function that returns a list of all the positive numbers in a list. Your function should only return the list.
Sample List : [-2, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


</text>
<cell>
# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: list_positive
def list_positive(some_list):
    '''
    Input: 
        some_list - a list of any numbers
    Output: 
        positive_list - a list of the positive numbers in some_list
    '''
    positive_list = []
    for num in some_list:
        if num > 0:
            positive_list.append(num)
    return positive_list

# Test your function
some_list = [-2, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
positive_list = list_positive(some_list)
print(positive_list)
</cell>
<text>
Expected output
[2, 5, 89]

</text>
<text>
Exercise 5
Write a function that returns a list of all the negative numbers in a list. Your function should only return the list.
Sample List : [-2, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


</text>
<cell>
# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: list_negative
def list_negative(some_list):
    '''
    Input: 
        some_list - a list of any numbers
    Output: 
        negative_list - a list of the negative numbers in some_list
    '''
    negative_list = []
    for num in some_list:
        if num < 0:
            negative_list.append(num)
    return negative_list

# Test your function
some_list = [-2, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
negative_list = list_negative(some_list)
print(negative_list)
</cell>
<text>
Expected output
[-2, -1, 89]

</text>
<text>
Exercise 6
Write a function that returns a new list with 4 elements:

The first element of the list is the sum of the first 2 numbers in the original list
The second element of the list is the sum of the first 3 numbers in the original list
The third element of the list is the sum of the first 4 numbers in the original list
The fourth element of the list is the first element in the original list

For example, list_sum([-2, -1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) is equal to [-2, -3, -6, -10, -15, -20, -26, -30, -35, -40, -45]

Hint: 