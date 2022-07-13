
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest first value.
    """
    return max(lst)[2]

# Test your function
print(tuple_extract(lst))
</cell>
<text>
Expected output
12
Explanation
The third value of the tuple with the largest first value is 12.

</text>
<text>


Exercise 7
Write a function that returns a list of numbers that represent how many times a value appears in a list. For example, how many times does the value 5 appear in the list [1, 1, 5, 6, 5, 5, 5] ? Your function should return a list that contains the number of times each value appears in the given list.

HINT: You can use a for loop!


</text>
<cell>
# UNQ_C7 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: count_elements
def count_elements(my_list):
    '''
    Input: a list of ints
    Output: a list of ints showing the number of times each int appears
    '''
    # Initialize count_list to count the number of times each int appears
    count_list = []
    
    # for each number in my_list...
    for number in my_list:
        # If number in count_list, increment the count for number
        if number in count_list:
            count_list[number] += 1
        # Otherwise, set the count to 1 for number
        else:
            count_list[number] = 1
    
    return count_list

# Test your function
print(count_elements([5, 2, 2, 4, 6, 2]))
</cell>
<text>
Expected output
[2, 4, 1, 2]

</text>
<text>


Exercise 8
Write a function that returns a list of all the even numbers from 0 to 20. Your function should return a list of all the even numbers from 0 to 20.

HINT: You can use the range() function!


</text>
<cell>
# UNQ_C8 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: even_numbers
def even_numbers(N):
    '''
    Input: an integer greater than 0
    Output: a list of numbers, starting from 0 to N - 1, that are even
    '''
    # Initialize an empty list
    even_numbers = []
    
    # loop from 0 to N-1
    for i in range(N):
        # If i is evenly divisible by 2...
        if i % 2 == 0:
            # Add i to even_numbers
            even_numbers.append(i)
            
    return even_numbers

# Test your function
even_numbers(10)
</cell>
<text>
Expected output
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

</text>
<text>


Exercise 9
Write a function that returns a list of all the odd numbers from 0 to 20. Your function should return a list of all the odd numbers from 0 to 20.

